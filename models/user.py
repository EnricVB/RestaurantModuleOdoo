from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import re

class User(models.Model):
    _name = 'restaurant.user'
    _description = 'Users from application'

    dni = fields.Char(string="DNI", required = True, unique = True)
    name = fields.Char(string="Name", required = True)
    birthDate = fields.Date(string="Date of birth")
    phone = fields.Char(string="Phone")

    @api.constrains('dni')
    def validateDni(self):
        if self.dni:
            dni_pattern = r'^\d{8}[A-Za-z]$'
            if not re.match(dni_pattern, self.dni):
                self.dni = ''
                raise ValidationError('The DNI format is invalid. It must be 8 digits followed by a letter (e.g., 12345678A).')

    @api.onchange('birthDate')
    def validateDate(self):
        if self.birthDate:
            if self.getAge() < 16:
                self.birthDate = ''
                return {
                    'warning': {
                        'title': "Underage",
                        'message': "User must be at least 16yo.",
                    }
                }
        

    @api.onchange('phone')
    def validatePhone(self):
        if(isinstance(self.phone, str)):
            self.phone = ''.join(self.phone.split()).replace(' ', '')
            isNumeric = self.phone.isnumeric()

            if(not isNumeric):
                self.phone = ''
                return {
                    'warning': {
                        'title': "Warning",
                        'message': f"Phone must not have characters or country id (+34).\nTry writting it again",
                    }
                }
            
            self.formatPhone()


    def formatPhone(self):
        if isinstance(self.phone, str):
            trimedPhone = self.phone.strip()

            self.phone = f"+34 {trimedPhone[:3]} {trimedPhone[3:5]} {trimedPhone[5:7]} {trimedPhone[7:]}"

    def getAge(self):
        today = date.today()
        age = today.year - self.birthDate.year - (
            (today.month, today.day) < (self.birthDate.month, self.birthDate.day)
        )
        return age

    @api.constrains('dni')
    def _check_dni_unique(self):
        for record in self:
            if self.search_count([('dni', '=', record.dni), ('id', '!=', record.id)]):
                raise ValidationError('DNI is already added.')