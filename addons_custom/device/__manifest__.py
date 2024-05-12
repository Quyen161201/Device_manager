# -*- coding: utf-8 -*-

{
    'name': 'Device Management',
    'description': 'Quản lý thiết bị',
    'summary': 'Device Management',
    'category': 'Construction',
    "sequence": 1,
    'version': '1.0.0',
    'author': 'Khả Quyền',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/device_main.xml',
        'views/device_extra.xml',
        'views/device_parts_in.xml',
        'views/device_product.xml',
        'data/device_sequence.xml',
        'views/menu.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
