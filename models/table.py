from odoo import models, fields, api
from datetime import datetime, timedelta

class Table(models.Model):
    _name = 'restaurant.table'
    _description = 'restaurant.table'

    tableNumber = fields.Integer(string="Table identify number", required=True, unique=True)
    local = fields.Many2one('restaurant.local', string="Local which this table belongs", required=True)
    chairs = fields.Integer(string="Number of chairs per table", required=True)

    book = fields.One2many(comodel_name = "restaurant.book", string = "Books of this table", inverse_name="table")
    bookTableOccupancy = fields.Integer(string = "Table occupancy at actual book", compute = "_ocuppancyPerDate")


    @api.depends('book.date','book.tableOcupancy')
    def _ocuppancyPerDate(self):
        now = datetime.now()
        for table in self:
            if not table.book:  # Si no hay reservas, asignar 0
                table.bookTableOccupancy = 0
                continue

            # Filtramos las reservas activas (en la última hora)
            active_books = table.book.filtered(lambda b: b.date and (b.date <= now <= (b.date + timedelta(hours=1))))
            
            table.bookTableOccupancy = active_books[0].tableOcupancy if active_books else 0  # Primera reserva activa o 0

    

    _sql_constraints = [
        ('table_number_local_unique', 'UNIQUE(tableNumber, local)', 'There can be just one same table number per local.')
    ]