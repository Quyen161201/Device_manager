from odoo import fields, models, api


class DeviceProduct(models.Model):
    _name = 'device.product'
    _description = 'Device product'

    name = fields.Char("Phân loại", required = True)
    device_group_ids = fields.One2many("device.group",'device_product_id')
