# Copyright (c) 2024, Priyanshu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Driver(Document):
	def validate(self):
		self.full_name = f"{self.first_name} {self.middle_name} {self.last_name}"
