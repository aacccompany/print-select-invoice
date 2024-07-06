# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime




class AACCAccountMove(models.Model):
    _name = 'aacc.account.move'

    def printSelectedInvoices(self):
        return self.export_report(self._context.get('active_ids', []))

   
    def export_report(self,ids):
            data = {
                'ids': ids,
                'model': "account.move"
            }
            
            return self.env.ref('aacc_invoice_reports.invoices_report').report_action(self,data=data)
            

class AACCInvoicesReportView(models.AbstractModel):
    """Abstract Model for report template.
    for `_name` model, please use `report.` as prefix then add `module_name.report_name`.
    """

    _name = 'report.aacc_invoice_reports.invoices_report_view'

    @api.model
    def _get_report_values(self,docids, data=None):
        account_moves = self.env['account.move'].browse(data["ids"])
    
        total_amount = 0

        for move in account_moves:
            total_amount += move.amount_total

        summary = {
            "total_amount":total_amount,
        }

        return {
            'doc_model': "account.move",
            'docs': account_moves,
            'summary' :summary
        }
