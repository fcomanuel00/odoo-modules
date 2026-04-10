{
    'name': 'Invoice Brand Selector',
    'version': '19.0.2.0.0',
    'summary': 'Manage multiple commercial brands on customer invoices',
    'description': '''
Invoice Brand Selector
======================

Allows you to configure multiple commercial brands with their own logo,
colors, email, website and footer. On each customer invoice, simply select
the brand and the PDF will be generated with the correct identity.

Features
--------
* Unlimited commercial brands
* Per-brand logo, colors, contact info and footer
* Brand selector on every customer invoice
* Dynamic PDF layout (logo + footer)
* Access control: managers configure, users select
* Compatible with Bubble layout

Use case
--------
Perfect for companies that operate under multiple commercial brands
but share the same legal entity and accounting.
    ''',
    'author': 'Framarketing',
    'maintainer': 'Framarketing',
    'website': 'https://framarketing.es',
    'category': 'Invoicing',
    'license': 'OPL-1',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/brand_profile_views.xml',
        'views/account_move_views.xml',
        'report/report_brand_layout.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 49.00,
    'currency': 'EUR',
}
