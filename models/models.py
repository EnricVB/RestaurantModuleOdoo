# from odoo import models, fields, api


# class Model(models.Model):
#     _name = 'module.model'
#     _description = 'module.model'

#     name = fields.Char(string="Variable description", required=False)
#     quantity = fields.Integer(store=False)
#     relation = fields.Many2one('module.model', string="Variable description", required=True)
#     multipleOptions = fields.Selection(string="description", selection=[{"1", "Type 1"}, {"2", "Type 2"}, {"3", "Type 3"}, {"4", "Type 4"}], defualt="1") 


#    @api.onchange('name', 'quantity', 'relation') # This is called on value change
#    def _onchange(self):
#       code...                
#       raise ValueError("Mensaje de error") # This is used in case you want to display an error message to user


#    @api.depends('name', 'quantity', 'relation') # This is called on save
#    def _depends(self):
#       code...

#    _sql_constraints = [
#       ('name_unique', 'UNIQUE(name)', 'Mensaje de error')
#    ]