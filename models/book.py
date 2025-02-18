from odoo import models, fields, api


class Book(models.Model):
    _name = 'restaurant.book'
    _description = 'Book made by client'

    name = fields.Char(compute="_nameCompute")

    table = fields.Many2one(comodel_name = "restaurant.table", string="Table", required = True, ondelete="cascade")
    date = fields.Datetime(string = "Date of book with hour", required = True)
    client = fields.Many2one('restaurant.client', string = "Client")
    tableOccupancy = fields.Integer(string = "Table Occupancy")

    @api.model
    def _nameCompute(self):
        for table in self:
            table.name = f"{table.client.name} Book: {table.table.name}"

    @api.model
    def create(self, vals):
        book = super(Book, self).create(vals)

        if book.table:
            book.table.write({'book': [(4, book.id)]})
        
        return book
    
