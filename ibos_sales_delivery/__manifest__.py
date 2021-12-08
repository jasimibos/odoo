# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'iBOS Sales Delivery',
    'version': '1.1',
    'summary': 'Report',
    'sequence': 20,
    'description': """ """,
    'category': '',
    'website': '',
    'images': [],
    'depends': ['base',
                'stock',
                ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sales_delivery.xml',
        'views/menu.xml',
        'report/report.xml',
        'report/sales_delivery_details.xml'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
