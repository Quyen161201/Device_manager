import base64

from odoo import fields, models, api
from odoo.modules import get_module_resource


class DevicePartsIn(models.Model):
    _name = 'device.parts.in'
    _inherit = 'device.device'
    _description = 'Linh kiện thiết bị'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('device', 'static/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char('Tên thiết bị', required=True)
    code = fields.Char('Mã thiết bị',required = True)
    main_device_id = fields.Many2one('device.main','Thiết bị chính', required = True)
    extra_device_id = fields.Many2one('device.extra',"Thiết bị phụ tùng", required = True,)
    amount = fields.Integer('Số lượng', default=1)
    price = fields.Integer('Giá', default=0)
    partner = fields.Char('Nhà cung cấp')
    image_1920 = fields.Binary(default=_default_image, store=True)
    description_images_ids = fields.One2many('device.image', 'parts_in_device_id', 'Hình ảnh mô tả')

    def open_liquidate(self):
        self.status = 'liquidate'

    def open_is_broken(self):
        self.status = 'is_broken'

    def open_loss(self):
        self.status = 'loss'

    def open_using(self):
        self.status = 'using'