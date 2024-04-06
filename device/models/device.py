from odoo import fields, models, api


class Device(models.Model):
    _name = 'device.device'
    _description = 'Thiết bị'

    date_import = fields.Date('Ngày nhập hàng', default=fields.Date.today(), track_visibility='onchange')
    first_date_use = fields.Date('Ngày đưa vào sử dụng', default=fields.Date.today(), track_visibility='onchange')
    period = fields.Integer("Bảo hành(Tháng)")
    description = fields.Html("mô tả")
    status = fields.Selection(
        [('not_used', 'Chưa sử dụng'), ('using', 'Đang sử dụng'), ('out_of_warranty', 'Hết bảo hành'),
         ('liquidate', 'Chờ thanh lý'), ('is_broken', 'Đang hỏng'), ('loss', 'Bị mất')], string='Trạng thái',
        required=True, default='not_used', track_visibility="onchange")


class DeviceImage(models.Model):
    _name = 'device.image'
    _description = 'Image device'
    name = fields.Char('name')
    image = fields.Binary('Image')
    description = fields.Text('Mô tả')
    main_device_id = fields.Many2one('device.main')
    extra_device_id = fields.Many2one('device.extra')
    parts_in_device_id = fields.Many2one('device.parts.in')


# class Attachment(models.Model):
#     _inherit = 'ir.attachment'
#     date = fields.Date('Attachment date', default=lambda self: fields.Date.today())
