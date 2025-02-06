# -*- coding: utf-8 -*-
# from odoo import http


# class Book-library(http.Controller):
#     @http.route('/book-library/book-library', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/book-library/book-library/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('book-library.listing', {
#             'root': '/book-library/book-library',
#             'objects': http.request.env['book-library.book-library'].search([]),
#         })

#     @http.route('/book-library/book-library/objects/<model("book-library.book-library"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('book-library.object', {
#             'object': obj
#         })
