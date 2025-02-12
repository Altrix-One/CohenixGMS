import frappe
from frappe.model.document import Document
import re

class Owner(Document):
    def validate(self):
        # Validate email format
        if self.owner_email and not re.match(r"[^@]+@[^@]+\.[^@]+", self.owner_email):
            frappe.throw("Invalid email format")
        
        # Validate SA ID Number format (example validation, adjust as needed)
        if self.owner_sa_id_number and not re.match(r"^\d{13}$", self.owner_sa_id_number):
            frappe.throw("Invalid SA ID Number format")
