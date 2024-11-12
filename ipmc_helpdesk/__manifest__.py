# -*- coding: utf-8 -*-
{
    'name': "help_desk_custom",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.0.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base','ipmc_helpdesk_customs'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/helpdesk_ticket_view.xml',
    ],

    # 'assets': {
    #     'web.assets_backend': ['app_one/static/src/css/property.css'],
    #     'web.assets_backend': ['app_one/static/src/css/building.css'],
    #     'web.report_assets_common': ['app_one/static/src/css/font.css'],
    #
    # },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}

