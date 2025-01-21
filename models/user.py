from odoo import models, fields, api


class User(models.Model):
    _name = 'restaurant.user'
    _description = 'Users from application'

    dni = fields.Char(string="DNI", required = True, unique = True)
    name = fields.Char(string="Name", required = True)
    birthDate = fields.Integer(string="Date of birth")
    phone = fields.Char(string="Phone")

    @api.onchange('dni')
    def _onchange_validateDni(self):
        # VALIDATE DNI
        return True

    @api.onchange('birthDate')
    def _onchange_validateBirthDate(self):
        # VALIDATE DATE OF BIRTH
        return True

    def getAge(self):
        # CALCULATE AGE BY BIRTHDATE
        return 18

    _sql_constraints = [
        ('dni_unique', 'UNIQUE(dni)', 'DNI is already added')
    ]
    