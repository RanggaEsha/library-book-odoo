# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Title')
    author_id = fields.Many2one('library.author', string='Author')
    price = fields.Float(string='Price')
    is_discounted = fields.Boolean(string='Is Discounted', compute='_compute_is_discounted')

    @api.depends('price')
    def _compute_is_discounted(self):
        for book in self:
            if book.price > 50:
                book.is_discounted = True
            else:
                book.is_discounted = False

    @api.constrains('price')
    def _check_price(self):
        for book in self:
            if book.price <= 0:
                raise ValidationError("price cannot be 0 or lower")