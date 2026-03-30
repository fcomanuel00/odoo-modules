# Copyright (C) 2026 Francisco Manuel Rodriguez
# Maintained by Framarketing (framarketing.es) · Romatel Global SL <info@framarketing.es>
# License OPL-1 (https://www.odoo.com/documentation/user/legal/licenses.html)

from odoo import models, fields, api


class BrandProfile(models.Model):
    _name = 'brand.profile'
    _description = 'Commercial Brand Profile'
    _order = 'sequence, name'

    name = fields.Char(string='Brand Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(default=True)

    # Visual identity
    logo = fields.Binary(string='Logo', attachment=True)
    primary_color = fields.Char(
        string='Primary Color',
        default='#875A7B',
        help='Header table color. Hex format: #RRGGBB',
    )

    # Contact info
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    phone = fields.Char(string='Phone')
    vat = fields.Char(string='Tax ID')

    # Custom footer (overrides individual fields if filled)
    footer_text = fields.Text(
        string='Custom Footer Text',
        help='If filled, replaces email/website/phone in the PDF footer.',
    )

    # Stats
    invoice_count = fields.Integer(
        string='Invoices',
        compute='_compute_invoice_count',
    )

    @api.depends('active')
    def _compute_invoice_count(self):
        for rec in self:
            rec.invoice_count = self.env['account.move'].search_count([
                ('brand_id', '=', rec.id),
                ('move_type', 'in', ['out_invoice', 'out_refund', 'out_receipt']),
            ])

    def action_view_invoices(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': f'Invoices - {self.name}',
            'res_model': 'account.move',
            'view_mode': 'list,form',
            'domain': [('brand_id', '=', self.id)],
            'context': {'default_brand_id': self.id},
        }
