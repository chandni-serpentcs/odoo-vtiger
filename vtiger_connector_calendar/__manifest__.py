# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': 'Calendar VTiger Integration',
    'version': '10.0.1.0.0',
    'summary': 'Calendar VTiger Integration',
    'description': """
        Calendar VTiger Integration""",
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'category': 'Marketing',
    'license': 'AGPL-3',
    'depends': ['calendar',
                'vtiger_connector_base'],
    'data': ['views/res_company_view.xml',
             'views/calendar_views.xml'],
    'installable': True,
}
