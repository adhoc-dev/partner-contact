# -*- coding: utf-8 -*-
# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
try:
    from openupgradelib import openupgrade
except ImportError:
    openupgrade = None


model_renames = [
    ('afip.document_type', 'res.partner.id_category'),
]


table_renames = [
    ('afip_document_type', 'res_partner_id_category'),
]


def pre_init_hook(cr):
    openupgrade.rename_models(cr, model_renames)
    openupgrade.rename_tables(cr, table_renames)
