from odoo import models, fields, api


class LocalOwner(models.Model):
    _name = 'restaurant.local_owner'
    _description = 'Local owner user'
    _inherit = 'restaurant.user'

    name = fields.Char(string="Name")
    dni = fields.Char(string="DNI", required = True, unique = True)
    phone = fields.Char(string="Phone", unique = False, required = False)
    birthDate = fields.Date(string = "Date of birth", required = False)
    
    local = fields.Many2many(comodel_name = "restaurant.local", string = "Local")
    employees = fields.Many2many('restaurant.employee', string="Employees of a local owner")
