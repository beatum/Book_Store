# -*- coding: utf-8 -*-
from openerp import http
from openerp.http import request

class main(http.Controller):
	@http.route('/book_store', type='http', auth='none')
	def books(self):
		records = request.env['library.book'].sudo().search([])
		result = '<html><body><table><tr><td>'
		result += '</td></tr><tr><td>'.join(
				records.mapped('name')
			)
		result += '</td></tr><//table></body></html>'

		return result
		
	@http.route('/book_store/books/json', type='json', auth='none')
	def books_json(self):
		records=request.env['library.book'].sudo().search([])

		return records.read(['name'])
		pass

