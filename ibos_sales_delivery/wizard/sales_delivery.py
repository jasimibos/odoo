# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class DeliveryPendingWizard(models.TransientModel):
    _name = "sales.delivery.wizard"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    location = fields.Many2one('stock.location', string="Source Location")

    def action_sales_delivery(self):
        data = {
            'model': 'stock.picking',
            'form_data': self.read()[0],
        }

        sales = self.env['stock.picking'].search([('location_id', '=', self.location.id),
                                                  ('scheduled_date', '>=', self.start_date),
                                                  ('date_deadline', '<=', self.end_date)])

        sales_details = []
        for sale in sales:
            sales_move = {}
            for sale_move in sale.move_ids_without_package:
                sales_move = {
                    'product_id': sale_move.product_id.name,
                    'product_qty': sale_move.product_qty,
                    'location_id': sale.location_id.complete_name,
                    'origin': sale.origin,
                    'scheduled_date': sale.scheduled_date,
                    'date_deadline': sale.date_deadline,
                    'state': sale.state,
                    'name': sale.name,
                }
                sales_details.append(sales_move)
                data['sales'] = sales_details

        return self.env.ref('ibos_sales_delivery.action_sales_delivery').report_action(self, data=data)
