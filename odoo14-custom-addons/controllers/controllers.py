# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo14-custom-addons/(http.Controller):
#     @http.route('/odoo14-custom-addons//odoo14-custom-addons//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo14-custom-addons//odoo14-custom-addons//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo14-custom-addons/.listing', {
#             'root': '/odoo14-custom-addons//odoo14-custom-addons/',
#             'objects': http.request.env['odoo14-custom-addons/.odoo14-custom-addons/'].search([]),
#         })

#     @http.route('/odoo14-custom-addons//odoo14-custom-addons//objects/<model("odoo14-custom-addons/.odoo14-custom-addons/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo14-custom-addons/.object', {
#             'object': obj
#         })
