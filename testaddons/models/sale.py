# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    _inherit = "sale.order"

    sale_description =fields.Char(string="Sale Description")
