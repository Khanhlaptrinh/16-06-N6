# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolInformation(models.Model):
    _name = 'shool.information'
    _description = 'School Management'

    name = fields.Char(string='Tên trường')
    type = fields.Selection([('private', 'Dân lập'), ('public', 'Công lập')], default='public', string='Loại trường')
    email = fields.Text(string='Email')
    address = fields.Text(string='Dia chi')

