from odoo import http
from odoo.http import request

class HospitalVitalsController(http.Controller):

    @http.route('/api/hospital/vitals/update', type='json', auth='public', methods=['POST'], csrf=False)
    def update_vitals(self, ticket_id=None, heart_rate=None, **kwargs):
        ticket = request.env['crm.lead'].sudo().search([('id', '=', ticket_id)], limit=1)
        if not ticket:
            return {'status': 'error', 'message': 'Ticket not found'}
        ticket.write({'patient_heart_rate': heart_rate})
        return {'status': 'ok', 'ticket_id': ticket_id, 'heart_rate': heart_rate}
