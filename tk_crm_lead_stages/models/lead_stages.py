# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LeadStages(models.Model):
    """
    LeadStages is used to display the stages of leads in
    the 'crm.lead' module, where the lead type is 'lead'.
    """
    _name = 'lead.stages'
    _description = "Lead Stages"
    _order = "sequence, name, id"

    name = fields.Char(string='Stage Name')
    sequence = fields.Integer(string='Sequence')
    is_won = fields.Boolean(string='Is Won Stage?')

    @api.constrains('is_won')
    def _check_only_one_won_stage(self):
        """
            Raises a validation error if the user sets more than one is_won boolean to true.
        """
        for record in self:
            if record.is_won:
                won_one_record = self.search([('is_won', '=', True),
                                              ('id', '!=', record.id)], limit=1)
                if won_one_record:
                    raise ValidationError("Only one stage can be marked as 'Is Won Stage'.")
