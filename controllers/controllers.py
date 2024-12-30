# -*- coding: utf-8 -*-
# from odoo import http


# class Isp(http.Controller):
#     @http.route('/isp/isp', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/isp/isp/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('isp.listing', {
#             'root': '/isp/isp',
#             'objects': http.request.env['isp.isp'].search([]),
#         })

#     @http.route('/isp/isp/objects/<model("isp.isp"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('isp.object', {
#             'object': obj
#         })

