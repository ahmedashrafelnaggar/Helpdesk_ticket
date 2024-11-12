# -*- coding: utf-8 -*-
# from odoo import http


# class IpmHelpdesk(http.Controller):
#     @http.route('/ipm_helpdesk/ipm_helpdesk', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ipm_helpdesk/ipm_helpdesk/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ipm_helpdesk.listing', {
#             'root': '/ipm_helpdesk/ipm_helpdesk',
#             'objects': http.request.env['ipm_helpdesk.ipm_helpdesk'].search([]),
#         })

#     @http.route('/ipm_helpdesk/ipm_helpdesk/objects/<model("ipm_helpdesk.ipm_helpdesk"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ipm_helpdesk.object', {
#             'object': obj
#         })
