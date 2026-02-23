# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ReferencedArticle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		article: DF.Link | None
		batch_no: DF.Data | None
		cdl: DF.Date | None
		next_rv: DF.Date | None
		place: DF.Link | None
		serial_no: DF.Data | None
	# end: auto-generated types

	pass
