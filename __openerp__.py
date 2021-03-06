# -*- coding: utf-8 -*-
{
    'name': "Book Store",

    'summary': """
            Manage Your Books
        """,

    'description': """
        Manage your Books, share your books, comment about your books.

        **Live Happy**  .. image:: http://localhost:8069/book_store/static/description/smile1.jpg

        

    """,

    'author': "Daniel Mutwiri",
    'website': "http://www.otbafrica.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','decimal_precision'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}