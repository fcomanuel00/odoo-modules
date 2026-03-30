# Copyright (C) 2026 Francisco Manuel Rodriguez
# Maintained by Framarketing (framarketing.es) · Romatel Global SL <info@framarketing.es>
# License OPL-1 (https://www.odoo.com/documentation/user/legal/licenses.html)

from odoo import models, fields


class AccountMove(models.Model):
    _inherit = 'account.move'

    brand_id = fields.Many2one(
        comodel_name='brand.profile',
        string='Commercial Brand',
        domain=[('active', '=', True)],
        tracking=True,
    )
