# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo14-custom-addons/(models.Model):
#     _name = 'odoo14-custom-addons/.odoo14-custom-addons/'
#     _description = 'odoo14-custom-addons/.odoo14-custom-addons/'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
