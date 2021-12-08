# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class CreateAppointmentWizard(models.Model):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    patient_name = fields.Char(string='Name')

    def action_create_appointment(self):
        print("Button Is Clicked")
