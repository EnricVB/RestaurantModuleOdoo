# -*- coding: utf-8 -*-
{
    'name': "restaurant",

    'summary': """
        A restaurant for booking clients/tables for multiple restaurants
    """,

    'description': """
    """,

    'author': "Enric Velasco Bufi and Cesar Abad Velasco",
    'website': "https://github.com/EnricVB/RestaurantModuleOdoo",

    'category': 'Application',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/user.xml',
        'views/client.xml',
        'views/local.xml',
        'views/employee.xml',
        'views/table.xml',
        'views/book.xml',
        'views/menus.xml',
    ],
    'demo': [
    ],
    'pip': [

    ],
    'assets': {
        'web.assets_backend': [
            'restaurant/static/img/mesa.png',
            'restaurant/static/img/silla.png',
        ],
    },


    'application': True,
}