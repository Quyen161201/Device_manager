from odoo import fields, models, api


class DeviceGroup(models.Model):
    _name = 'device.group'
    _description = 'Device group'
    name = fields.Char("Nhóm thiết bị")
    device_product_id = fields.Many2one("device.product",'Phân loại')

