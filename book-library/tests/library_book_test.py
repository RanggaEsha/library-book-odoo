# -*- coding: utf-8 -*- 
from odoo.exceptions import ValidationError

from odoo.tests import common 

class TestLibraryBook(common.TransactionCase):
    def test_price_data(self):
        test_price = self.env['library.book'].create({'Title':'Test Book'},{'price':'0'})

        self.assertEqual(test_price, "price cannot be 0 or lower")
        print('Your test was succesfull!')
    
    # def test_compute_book_number(self):
    #     book_number = 