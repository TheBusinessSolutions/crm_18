{
    'name': 'CRM Lost Reason Required',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Enforce Lost Reason selection when marking a Lead/Opportunity as lost.',
    'description': """
        This module ensures that users must select a Lost Reason 
        when marking a CRM Lead or Opportunity as lost.
    """,
    'author': 'BUsiness Solutions',
    'website': 'https://www.thebusinesssolutions.net',
    'license': 'LGPL-3',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_lost_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}