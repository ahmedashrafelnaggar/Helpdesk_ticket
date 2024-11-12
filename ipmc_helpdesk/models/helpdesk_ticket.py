from odoo import fields, models

class helpdesk_ticket(models.Model):
    _inherit = 'helpdesk.ticket'
    _description = "Helpdesk ticket"

    mualamah = fields.Char()
    oolweh_mualamah_priority = fields.Selection(
        [
            ('عاجل', 'عاجل'),
            ('عاجل جدا وهام', 'عاجل جدا وهام'),
            ('عاجل جدا وهام يسلم حالا', 'عاجل جدا وهام يسلم حالا'),
            ('سري', 'سري'),
            ('سري-عاجل جدا وهام', 'سري-عاجل جدا وهام'),
            ('يفتح بيد سعادته', 'يفتح بيد سعادته'),
        ],
        string="اولويه المعامله"
    )

