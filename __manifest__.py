# Copyright 2020 Iván Todorovich
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "AACC Invoice Reports",
    "summary": "AACC Invoice Custom Reports",
    "version": "17.0.0.0.0",
    "category": "Sales",
    "website": "https://aacc-th.com/",
    "author": "AACC Thailand.",
    "license": "AGPL-3",
    "development_status": "Production/Stable",
    "depends": ["account"],
    "data": [
            "views/invoice_printing.xml",
            "reports/invoices_report.xml",
            "security/ir.model.access.csv"
        ],
    "installable": True,
}