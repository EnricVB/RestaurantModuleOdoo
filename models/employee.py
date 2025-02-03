from odoo import models, fields, api


class Employee(models.Model):
    _name = 'restaurant.employee'
    _description = 'Employee user'
    _inherit = 'restaurant.user'

    name = fields.Char(string="Name")
    dni = fields.Char(string="DNI", required = True, unique = True)
    image = fields.Binary(string="Image URL")

    birthDate = fields.Date(string = "Date of birth")
    phone = fields.Char(string="Phone")

    local = fields.Many2many(comodel_name="restaurant.local", string = "Local")