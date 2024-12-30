# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    connection_ids = fields.One2many('isp.connection', 'customer_id', string="Conexiones")

class ISPConnection(models.Model):
    _name = 'isp.connection'
    _description = 'Conexión de ISP'

    name = fields.Char(string="Nombre de la Conexión", required=True)
    customer_id = fields.Many2one('res.partner', string="Cliente", required=True)
    plan_id = fields.Many2one('isp.plan', string="Plan", required=True)
    device_id = fields.Many2one('isp.device', string="Dispositivo (ONU)", required=True)

class ISPPlan(models.Model):
    _name = 'isp.plan'
    _description = 'Plan de Internet'

    name = fields.Char(string="Nombre del Plan", required=True)
    download_speed = fields.Float(string="Velocidad de Descarga (Mbps)", required=True)
    upload_speed = fields.Float(string="Velocidad de Subida (Mbps)", required=True)
    price = fields.Float(string="Precio", required=True)
    active_clients_count = fields.Integer(string="Clientes Activos", compute='_compute_client_counts', store=True)
    suspended_clients_count = fields.Integer(string="Clientes Suspendidos", compute='_compute_client_counts', store=True)

    @api.depends('connection_ids')
    def _compute_client_counts(self):
        for plan in self:
            connections = self.env['isp.connection'].search([('plan_id', '=', plan.id)])
            plan.active_clients_count = len(connections.filtered(lambda c: c.state == 'active'))
            plan.suspended_clients_count = len(connections.filtered(lambda c: c.state == 'suspended'))

class ISPDevice(models.Model):
    _name = 'isp.device'
    _description = 'Dispositivo (ONU)'

    name = fields.Char(string="Nombre del Dispositivo", required=True)
    mac_address = fields.Char(string="MAC Address", required=True)
    ip_address = fields.Char(string="IP Address", required=True)
