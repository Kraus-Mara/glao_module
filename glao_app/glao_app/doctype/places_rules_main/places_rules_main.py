# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PlacesRulesMain(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from glao_app.glao_app.doctype.places_stock_rules.places_stock_rules import (
            PlacesStockRules,
        )
        from frappe.types import DF

        article: DF.Link | None
        table_cqxh: DF.Table[PlacesStockRules]
    # end: auto-generated types

    pass
