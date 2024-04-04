from odoo import fields, models, api
import qrcode
from io import BytesIO
import base64

from odoo.http import request
from odoo.modules.module import get_module_resource


def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()
    temp = BytesIO()
    img.save(temp, format="PNG")
    qr_img = base64.b64encode(temp.getvalue())
    return qr_img


class DeviceMain(models.Model):
    @api.model
    def _default_image(self):
        image_path = get_module_resource('device', 'static/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    _name = 'device.main'
    _inherit = 'device.device'
    _description = 'Device main'
    name = fields.Char('Tên thiết bị', required=True)
    default_code = fields.Char('Mã thiết bị', required=True, readonly=True, default='TB')
    print_name = fields.Char('Tên mã QR')
    quantity = fields.Integer('Số lượng')
    company_id = fields.Many2one('res.company', 'Công ty', default=lambda self: self.env.company)
    department_id = fields.Many2one('hr.department', 'Phòng ban', domain=[('company_id', '=', 'company_id')])
    employee_id = fields.Many2one('hr.employee', 'Nhân viên sử dụng',
                                  domain=[('department_id', 'child_of', 'department_id')])
    device_extra_ids = fields.One2many('device.extra','device_main_id','Thiết bị phụ tùng')
    image_1920 = fields.Binary(default=_default_image, store=True)
    qr_image = fields.Binary('QR code', compute='_generate_qr')
    description_images_ids= fields.One2many('device.image','main_device_id','Hình ảnh mô tả')

    @api.model
    def create(self, vals_list):
        if vals_list.get('default_code', ('_TB') == ('_TB')):
            vals_list['default_code'] = self.env['ir.sequence'].next_by_code('device.main')
        return super().create(vals_list)

    @api.onchange('name')
    def _print_name(self):
        if not self.print_name:
            self.print_name = self.name

    def _generate_qr(self):
        for item in self:
            base_url = request.env['ir.config_parameter'].sudo().get_param('web.base.url')
            base_url += '/web#id=%d&view_type=form&model=%s' % (item.id, item._name)
            item.qr_image = generate_qr_code(base_url)

    def open_liquidate(self):
        self.status = 'liquidate'

    def open_is_broken(self):
        self.status = 'is_broken'

    def open_loss(self):
        self.status = 'loss'

    def open_using(self):
        self.status = 'using'


class Department(models.Model):
    _inherit = ['hr.department']
    device_ids = fields.One2many('device.main', 'department_id', string='Thiết bị')
