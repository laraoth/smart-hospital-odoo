from odoo import models, fields, api

class CrmLeadPulse(models.Model):
    _inherit = 'crm.lead'

    patient_heart_rate = fields.Integer(string='Patient Heart Rate (BPM)')
    is_critical_iot_alert = fields.Boolean(string='Critical IoT Alert', default=False)

    def write(self, vals):
        result = super(CrmLeadPulse, self).write(vals)
        if 'patient_heart_rate' in vals:
            hr = vals['patient_heart_rate']
            if hr < 40 or hr > 140:
                super(CrmLeadPulse, self).write({
                    'priority': '3',
                    'is_critical_iot_alert': True,
                })
                self.message_post(body='SYSTEM OVERRIDE: CRITICAL VITALS DETECTED.')
        return result
