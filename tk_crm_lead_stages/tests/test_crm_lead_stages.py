# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged
from odoo.exceptions import ValidationError


@tagged('crm_lead_stages')
class TestCrmLeadStages(TransactionCase):
    """
    Test case for the 'CrmLeadStages' and 'LeadStages' model.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.env['lead.stages'].search([('is_won', '=', True)]).write({'is_won': False})

        cls.stage_one = cls.env['lead.stages'].create({
            'name': 'Demo 1',
            'sequence': 1,
            'is_won': False,
        })

        cls.stage_won = cls.env['lead.stages'].create({
            'name': 'Test Demo Won',
            'sequence': 3,
            'is_won': True,
        })

        cls.lead = cls.env['crm.lead'].create({
            'name': 'Test Lead 1',
            'type': 'lead',
        })

    def test_is_won_related_field(self):
        """
        Test that the `is_won` field on crm.lead is correctly linked to the lead_stage_id.
        """
        self.assertFalse(self.lead.is_won)
        self.lead.lead_stage_id = self.stage_won
        self.assertTrue(self.lead.is_won)

    def test_lead_won_stage_method(self):
        """
        Test the lead_won_stage method updates the lead_stage_id to the won stage.
        """
        self.lead.lead_stage_id = self.stage_one
        self.assertNotEqual(self.lead.lead_stage_id, self.stage_won)
        self.lead.lead_won_stage()
        self.assertEqual(self.lead.lead_stage_id, self.stage_won)

    def test_only_one_is_won_stage(self):
        """
        Ensure that only one stage can be set with is_won=True.
        """
        with self.assertRaises(ValidationError):
            self.env['lead.stages'].create({
                'name': 'Another Won',
                'sequence': 3,
                'is_won': True,
            })
