# -*- coding: utf-8 -*-

from openerp import models, fields, api


class LibraryBook(models.Model):
	_name='library.book'
	name = fields.Char('Title', required=True)
	date_release = fields.Date()
	authors_id = fields.Many2many('res.partner', string="Authors")