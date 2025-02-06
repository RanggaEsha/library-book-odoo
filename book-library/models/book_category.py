# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookCategory(models.Model):
    _name = 'book.category'
    _description = 'Book Category'

    name = fields.Char(string='Category Name')
    book_number = fields.Integer(string='Number of Books', compute="_compute_book_number")

    def _compute_book_number(self):
        for rec in self:
            rec.book_number = len(self.env['library.book'].search([('category_id', '=', rec.id)]))



