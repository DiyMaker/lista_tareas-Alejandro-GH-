# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo02(http.Controller):
#     @http.route('/ejemplo02/ejemplo02/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo02/ejemplo02/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo02.listing', {
#             'root': '/ejemplo02/ejemplo02',
#             'objects': http.request.env['ejemplo02.ejemplo02'].search([]),
#         })

#     @http.route('/ejemplo02/ejemplo02/objects/<model("ejemplo02.ejemplo02"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo02.object', {
#             'object': obj
#         })
