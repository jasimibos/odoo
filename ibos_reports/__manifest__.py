# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Delivery Report',
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
    'data': ['security/ir.model.access.csv',
             'wizard/delivery_pending.xml',
             'views/menu.xml',
             'report/report.xml',
             'report/report_details.xml',

             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
