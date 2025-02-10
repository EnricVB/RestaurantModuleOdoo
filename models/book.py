from odoo import models, fields, api


class Book(models.Model):
    _name = 'restaurant.book'
    _description = 'Book made by client'

    table = fields.Many2one(comodel_name = "restaurant.table", string="Table")
    date = fields.Datetime(string = "Date of book with hour", required = True)
    client = fields.Many2one(comodel_name="restaurant.client", string="Client")