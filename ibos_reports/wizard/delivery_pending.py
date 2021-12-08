# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class DeliveryPendingWizard(models.TransientModel):
    _name = "delivery.pending.wizard"
    _description = "Delivery Pending Wizard"

    start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now())
    end_date = fields.Datetime(string="End Date", default=fields.Datetime.now())
    location_id = fields.Many2one('stock.location', string='Source Location')


    def action_delivery_pending(self):

        delivery=self.env['stock.picking'].search_read([])
        # print("delivery....",delivery)
        data={
            'form_data':self.read()[0],
            'delivery':delivery
        }
        # print(data['delivery'])
        return self.env.ref('ibos_reports.action_report_by_payment_type').report_action(self, data=data)






        # data = {
        #     'model': 'delivery.pending.wizard',
        #     'form': self.read()[0]
        # }
        #
        # location_id = data['form']['location_id']
        # start_date = data['form']['start_date']
        # end_date = data['form']['end_date']
        # only_location_id = location_id[0]
        # data_report = self.env.cr.execute(
        #     f"""SELECT  sp.name as name, sp.scheduled_date as fromDate, sp.date_deadline, sl.name, sp.origin as origin ,sp.partner_id
        #         from stock_picking as sp
        #         LEFT JOIN stock_location as sl on sp.location_id=sl.id where  sp.date
        #         between '{start_date}' and '{end_date}'""")
        # result = self._cr.dictfetchall()
        # print(start_date)
        # print(end_date)
        # return self.env.ref('ibos_reports.action_report_by_payment_type').report_action(self, data=result)
