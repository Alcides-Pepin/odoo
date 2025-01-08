# -*- coding: utf-8 -*-

{
    'name': 'Website Event Recurring',
    'category': 'Marketing/Events',
    'version': '1.0',
    'summary': 'Make an event recurring.',
    'description': """
Make an event recurring.
    """,
    'author': 'Pépin, Alcides DE OLIVEIRA GUERRA',
    'depends': [
        'website_event', 
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/event_event_add.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
