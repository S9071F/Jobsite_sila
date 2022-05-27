# -*- coding: utf-8 -*-
from odoo import http

# class JobsiteSila(http.Controller):
#     @http.route('/jobsite_sila/jobsite_sila/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jobsite_sila/jobsite_sila/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jobsite_sila.listing', {
#             'root': '/jobsite_sila/jobsite_sila',
#             'objects': http.request.env['jobsite_sila.jobsite_sila'].search([]),
#         })

#     @http.route('/jobsite_sila/jobsite_sila/objects/<model("jobsite_sila.jobsite_sila"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jobsite_sila.object', {
#             'object': obj
#         })