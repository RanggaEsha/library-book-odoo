# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Library Book'

    title = fields.Char(string='Title')
    author_id = fields.Many2one('library.author', string='Author')
    price = fields.Float(string='Price')
    category_id = fields.Many2one('book.category', string='Category', required=True)

    @api.constrains('price')
    def _check_price(self):
        for book in self:
            if book.price <= 0:
                raise ValidationError("price cannot be 0 or lower")
            
    def compute_book_number_by_category(self):
        for book in self:
            body = _(f'The category {self.category_id.name} has {self.category_id.book_number} books')
            book.message_post(body=body)