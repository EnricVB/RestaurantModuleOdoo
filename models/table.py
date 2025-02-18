from odoo import models, fields, api
from datetime import datetime, timedelta

class Table(models.Model):
    _name = 'restaurant.table'
    _description = 'restaurant.table'

    name = fields.Char(compute="_nameCompute")

    tableNumber = fields.Integer(string="Table identify number", required=True)
    local = fields.Many2one('restaurant.local', string="Local which this table belongs", required=True)
    chairs = fields.Integer(string="Number of chairs per table", required=True)

    book = fields.One2many(comodel_name = "restaurant.book", string = "Books of this table", inverse_name="table")
    bookTableOccupancy = fields.Integer(string = "Table occupancy at actual book", compute = "_ocuppancyPerDate")

    @api.model
    def _nameCompute(self):
        for table in self:
            table.name = f"Table {table.tableNumber}"

    @api.depends('book.date', 'book.tableOccupancy')
    def _ocuppancyPerDate(self):
        now = datetime.now()
        for table in self:
            if not table.book:
                table.bookTableOccupancy = 0
                continue

            active_books = table.book.filtered(lambda b: b.date and (b.date <= now <= (b.date + timedelta(hours=1))))
            
            table.bookTableOccupancy = active_books[0].tableOccupancy if active_books else 0 

    _sql_constraints = [
        ('table_number_local_unique', 'UNIQUE(tableNumber, local)', 'There can be just one same table number per local.')
    ]