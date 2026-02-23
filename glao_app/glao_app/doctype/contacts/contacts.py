# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Contacts(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		add_notes: DF.Check
		address: DF.Data | None
		city: DF.Data | None
		country: DF.Data | None
		email: DF.Data
		lastname: DF.Data
		mobile: DF.Data | None
		notes: DF.LongText | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		phone: DF.Data | None
		postcode: DF.Data | None
		surname: DF.Data
	# end: auto-generated types

	pass
