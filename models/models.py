# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp.addons import decimal_precision as dp

class LibraryBook(models.Model):
	_name='library.book'
	_description = 'Library of Books'
	_order = 'date_release desc, name'
	_rec_name = 'short_name'

	_sql_constraints = [
			('name_uniq','UNIQUE (name)','Book Title Already Taken')
		]
	name = fields.Char('Title', required=True)
	short_name = fields.Char(string='Short Title',size=100, translate=False)
	date_release = fields.Date('Release Date')
	authors_id = fields.Many2many('res.partner', string="Authors")
	notes = fields.Text('Internal Notes')
	state = fields.Selection(
			[('draft','Not Available'),
				('available','Available'),
				('lost','Lost')],'State')
	cover = fields.Binary('Book Cover')
	out_of_print = fields.Boolean('Out of Print?')
	date_update = fields.Datetime('Last Update')
	pages = fields.Integer(string='Number of Pages',
			default=0,help="Total book page count",
			groups='base.group_user',
			states={'cancel': [('readonly',True)]},
			copy=True,
			index=False, 
			required=False,
			readonly=False,
			company_dependent=False,)
	reader_rating = fields.Float('Reader Average Rating',(14,4))
	description = fields.Html(string='Description',
								sanitize=True,
								strip_style=False,translate=False)
	cost_price = fields.Float('Book Cost', dp.get_precision('Book Price'))
	currency_id = fields.Many2one('res.currency', string='Currency')
	retail_price = fields.Monetary('Retail Price')
	publisher_id = fields.Many2one(
		'res.partner',string='Publisher',ondelete='set null',context={}, domain=[],)

	api.constrains('date_release')
	def _check_release_date(self):
		for r in self:
			if r.date_release > fields.Date.today():
				raise models.ValidationError(
						'Release Date must be in the past'
					)



class ResPartner(models.Model):
	_inherit='res.partner'
	books_ids = fields.One2many('library.book','publisher_id',string='Published Books')
	books_ids =fields.Many2many('library.book',string='Authored Books')