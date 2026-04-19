{
    'name': 'CRM Salesperson Required',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Make Salesperson (user_id) mandatory in CRM Leads and Opportunities',
    'description': """
        This module ensures that a Salesperson is assigned to every Lead or Opportunity.
        It adds a backend constraint and updates the form view to show the field as required.
    """,
    'author': 'Business Solutions',
    'website': 'https://www.thebusinesssolutions.net',
    'license': 'LGPL-3',
    'depends': [
        'crm',
    ],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}