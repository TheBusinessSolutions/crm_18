from odoo import models, api, _
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('user_id')
    def _check_salesperson_assigned(self):
        """
        Constraint to ensure user_id (Salesperson) is not empty.
        """
        for record in self:
            if not record.user_id:
                raise ValidationError(_("Please assign a Salesperson to this Lead/Opportunity before saving."))