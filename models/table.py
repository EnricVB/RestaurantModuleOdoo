from odoo import models, fields, api


class Table(models.Model):
    _name = 'restaurant.table'
    _description = 'restaurant.table'

    tableNumber = fields.Integer(string="Table identify number", required=True, unique=True)
    local = fields.Many2one('restaurant.local', string="Local which this table belongs", required=True)
    positionX = fields.Integer(string="X Position for visual purposes", required=True)
    positionY = fields.Integer(string="Y Position for visual purposes", required=True)
    chairs = fields.Integer(string="Number of chairs per table", required=True)

    book = fields.One2many(comodel_name = "restaurant.book", string = "Books of this table", inverse_name="table")

    _sql_constraints = [
        ('table_number_local_unique', 'UNIQUE(tableNumber, local)', 'There can be just one same table number per local.')
    ]