# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Nomenclature(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from glao_app.glao_app.doctype.nomenclature_items.nomenclature_items import (
            NomenclatureItems,
        )
        from frappe.types import DF

        is_active: DF.Check
        items: DF.Table[NomenclatureItems]
        nomenclature_name: DF.Data | None
    # end: auto-generated types

    pass
