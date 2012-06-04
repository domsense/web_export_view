# -*- coding: utf-8 -*-

{
    'name': 'Export Current View',
    'version': '1.0',
    'category': 'Web',
    'description': """ Adds a link in the right toolbar 
    for exporting current view (tree type only ATM) to XLS.
    """,
    'author': 'Simone Orsi - Domsense (simone.orsi@domsense.com)',
    'website': '',
    'license': 'AGPL-3',
    'depends': ['web'],
    'external_dependencies' : {
        'python' : ['xlwt'],
     },
    'data': [],
    'active': False,
    'auto_install': False,
    'js': [
        'static/js/web_advanced_export.js',
    ],
}

