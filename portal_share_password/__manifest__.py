# -*- coding: utf-8 -*-
{
    'name': "Grant Portal User With Password",

    'summary': """Add a password field in grant portal user dialog""",
    'description': """Share portal user with password""",

    'author': "xujl",
    'website': "http://www.pan-sen.com",

    'category': 'Uncategorized',
    'version': '12.0.1.0.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal'],

    # always loaded
    'data': [
        'data/res_config_data.xml',
        'wizard/portal_wizard_views.xml',
    ],
    'demo': [
    ],
}