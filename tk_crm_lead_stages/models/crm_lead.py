# -*- coding: utf-8 -*-
from odoo import fields, models, api


class CrmLeadStages(models.Model):
    """
        Inherits from 'crm.lead' to customize behavior or add additional fields.
    """
    _inherit = 'crm.lead'

    lead_stage_id = fields.Many2one('lead.stages', string='Lead Stage',
                                      default=lambda self: self._default_stage_id(), tracking=True)
    is_won = fields.Boolean(string='Is Won Stage?', related='lead_stage_id.is_won')

    def _default_stage_id(self):
        """
            Returns the stages of the leads.
        """
        return self.env['lead.stages'].search([], order='sequence', limit=1)

    @api.model
    def default_get(self, fields_list):
        """
        Overrides the default_get method to set the first lead stage
        (based on sequence) as the default for lead_stage_id.
        """
        defaults = super(CrmLeadStages, self).default_get(fields_list)

        if 'lead_stage_id' in fields_list:
            first_stage = self.env['lead.stages'].search([], order='sequence', limit=1)
            if first_stage:
                defaults['lead_stage_id'] = first_stage.id
        return defaults

    def lead_won_stage(self):
        """
            Returns the lead stages that only have is_won set to true.
        """
        won_stage = self.env['lead.stages'].search([('is_won', '=', True)], order='sequence')

        if won_stage:
            self.write({'lead_stage_id': won_stage.id})
