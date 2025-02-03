from odoo import models, fields, api


class Local(models.Model):
    _name = 'restaurant.local'
    _description = 'Physical local'

    name = fields.Char(string="Name", required=True)
    id = fields.Integer(string="ID", required = True, unique = True)
    direction = fields.Char(string = "Direction", required = True, unique = True)
    employees = fields.Many2many(comodel_name = "restaurant.employee", string = "Employees")

    
    @api.depends('employees')
    def _onAddEmployee(self):
        for local in self:
            for employee in local.employees:
                if local.id not in employee.local.ids:
                    employee.local = [(4, local.id)]
