from odoo import models, fields, api


class Client(models.Model):
    _name = 'restaurant.client'
    _description = 'Client user'
    _inherit = 'restaurant.user'

    name = fields.Char(string="Name")
    dni = fields.Char(string="DNI", required = True, unique = True)
    birthDate = fields.Date(string = "Date of birth", required = False)
    phone = fields.Char(string="Phone", unique = False, required = False)
    reservations = fields.Many2many(comodel_name = "restaurant.book", string = "Reservations")
    

