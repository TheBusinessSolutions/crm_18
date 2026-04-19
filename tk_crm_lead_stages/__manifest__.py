# -*- coding: utf-8 -*-
{
    'name': 'CRM Lead Stages | Lead Status',
    'description': """
        CRM Lead Stages
    """,
    'summary': 'CRM Lead Stages',
    'version': '1.0',
    'category': 'CRM',
    'author': 'TechKhedut Inc.',
    'company': 'TechKhedut Inc.',
    'maintainer': 'TechKhedut Inc.',
    'website': "https://techkhedut.com",
    'depends': [
        'crm',
    ],
    'data': [
        #  security
        'security/ir.model.access.csv',
        # data
        'data/lead_stages_demo.xml',
        #  views
        'views/lead_stages_views.xml',
        'views/crm_lead_views.xml',
        'views/menu.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
