# -*- coding: utf-8 -*-
from openerp import http

# class /opt/odoo/danAddons/bookStore(http.Controller):
#     @http.route('//opt/odoo/dan_addons/book_store//opt/odoo/dan_addons/book_store/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/dan_addons/book_store//opt/odoo/dan_addons/book_store/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/dan_addons/book_store.listing', {
#             'root': '//opt/odoo/dan_addons/book_store//opt/odoo/dan_addons/book_store',
#             'objects': http.request.env['/opt/odoo/dan_addons/book_store./opt/odoo/dan_addons/book_store'].search([]),
#         })

#     @http.route('//opt/odoo/dan_addons/book_store//opt/odoo/dan_addons/book_store/objects/<model("/opt/odoo/dan_addons/book_store./opt/odoo/dan_addons/book_store"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/dan_addons/book_store.object', {
#             'object': obj
#         })