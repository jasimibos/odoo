# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    patient_name = fields.Char(string='Name', required=True, copy=False)
    # patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)

    # Generate Sequential Value
    reference = fields.Char(string='Reference', required=True, copy=False, readonly=True,
                            default=lambda self: _('New'))
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], required=True, default='male', tracking=True)
    patient_age = fields.Integer(string='Age', tracking=True)
    note = fields.Char(string='Description')
    state = fields.Selection([('draft', 'Draft'),
                              ('confirm', 'Confirmed'),
                              ('done', 'Done'),
                              ('cancel', 'Cancelled')],
                             default='draft', string='Status', tracking=True)
    date_appointment = fields.Datetime(string='Date')

    # control statusbar

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

        # override create method

    @api.model
    def create(self, vals):
        if not vals.get('note'):
            vals['note'] = 'New Patient'
            # sequence value auto generate method
        if vals.get('reference', _('New')) == ('New'):
            vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res
