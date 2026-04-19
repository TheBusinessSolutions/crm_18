from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('lost_reason_id', 'active')
    def _check_lost_reason(self):
        """
        Safety net: Ensure that if a lead is marked as inactive (lost), 
        a lost reason must be specified.
        """
        for record in self:
            if not record.active and not record.lost_reason_id:
                raise ValidationError(_("Please specify a Lost Reason before marking this opportunity as lost."))


class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'

    # This line makes the field REQUIRED in the Wizard automatically
    # No XML needed for this to work in the UI
    lost_reason_id = fields.Many2one(required=True)