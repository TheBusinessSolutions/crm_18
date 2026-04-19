from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('lost_reason_id', 'active')
    def _check_lost_reason(self):
        """
        Ensure that if a lead is marked as inactive (lost), 
        a lost reason must be specified.
        """
        for record in self:
            # If the record is inactive (lost) and no reason is set
            if not record.active and not record.lost_reason_id:
                raise ValidationError(_("Please specify a Lost Reason before marking this opportunity as lost."))


class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    # Override the field to make it required by default in the wizard
    lost_reason_id = fields.Many2one(required=True)