from odoo import models, fields, api


class Local(models.Model):
    _name = 'restaurant.local'
    _description = 'Physical local'

    name = fields.Char(string="Name", required=True)
    id = fields.Integer(string="ID", required = True, unique = True)
    direction = fields.Char(string = "Direction", required = True, unique = True)
    employes = fields.Many2many(comodel_name = "restaurant.employee", string = "Employees")
