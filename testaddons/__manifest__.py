# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital',
    'version': '1.1',
    'summary': 'Hospital management software',
    'sequence': 20,
    'description': """ """,
    'category': 'Hostpital Management',
    'website': '',
    'images': [],
    'depends': ['sale',
                'mail',
                ],
    'data': ['security/ir.model.access.csv',
             'data/data.xml',
             'views/patient.xml',
             'views/kids.xml',
             'views/appointment.xml',
             'views/sale.xml',
             'wizard/create_appointment.xml',
             'reports/sales_report.xml',
             'reports/patient_card.xml',

             ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

}
