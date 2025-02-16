from odoo import models, fields, api


class Book(models.Model):
    _name = 'restaurant.book'
    _description = 'Book made by client'

    table = fields.Many2one(comodel_name = "restaurant.table", string="Table", required = True, ondelete="cascade")
    date = fields.Datetime(string = "Date of book with hour", required = True)
    client = fields.Many2one('restaurant.client', string = "Client")
    tableOcupancy = fields.Integer(string = "Table Ocupancy")

    @api.model
    def create(self, vals):
        """Al crear una reserva, aseguramos que la mesa la guarde en su One2many"""
        book = super(Book, self).create(vals)

        # Asegurar que la mesa guarda la reserva en su One2many
        if book.table:
            book.table.write({'book': [(4, book.id)]})  # Agrega la reserva a la mesa seleccionada
        
        return book
    
