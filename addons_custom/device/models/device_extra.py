import base64

from odoo import fields, models, api
from odoo.modules import get_module_resource


class ModelName(models.Model):
    _name = 'device.extra'
    _inherit = 'device.device'
    _description = 'Device extra'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('device', 'static/img', 'default_image.png')
        return base64.b64encode(open(image_path, 'rb').read())

    name = fields.Char('Tên thiết bị', required = True)
    code = fields.Char('Mã thiết bị', required= True)
    device_main_id = fields.Many2one('device.main','Thiết bị chính')
    amount = fields.Integer('Số lượng', default= 1)
    price = fields.Integer('Giá', default=0)
    partner = fields.Char('Nhà cung cấp')
    image_1920 = fields.Binary(default=_default_image, store=True)
    device_parts_in_ids = fields.One2many('device.parts.in','extra_device_id','Linh kiện thiết bị')
    description_images_ids= fields.One2many('device.image','extra_device_id','Hình ảnh mô tả')


    def open_liquidate(self):
        self.status = 'liquidate'

    def open_is_broken(self):
        self.status = 'is_broken'

    def open_loss(self):
        self.status = 'loss'

    def open_using(self):
        self.status = 'using'

