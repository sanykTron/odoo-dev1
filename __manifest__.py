# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Managment AR',
    'category': 'Extra Tools',
    'summary': 'A new app to manage a Hospital',
    'version': '12.0.0',
    'description': """This module adds a Twitter roller building block to the website builder, so that you can display Twitter feeds on any page of your website.""",
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/website_twitter_data.xml',
        'views/res_config_settings_views.xml',
        'views/website_twitter_snippet_templates.xml'
    ],
    'installable': True,
    'license': 'LGPL-3',
    'application' : True,
    'author': 'ARH+',
}





