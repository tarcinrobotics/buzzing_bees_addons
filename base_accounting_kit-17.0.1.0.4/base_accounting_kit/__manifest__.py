# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://tarcin.in>)
#    Author: Cybrosys Techno Solutions(<https://tarcin.in>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Tarcin Full Accounting Kit',
    'version': '17.0.1.0.4',
    'category': 'Accounting',
    'summary': """Tarcin Accounting, Tarcin Accounting Reports, Tarcin Accounting, tarcin Accounting, Tarcin Financial Reports, Tarcin Asset, Tarcin Profit and Loss, PDC, Followups, Tarcin, Accounting, tarcin Apps, Reports""",
    'description': """ Tarcin Accounting, The module used to manage the Full
     Account Features that can manage the Account Reports,Journals Asset and 
     Budget Management, Accounting Reports, PDC, Lock dates, Credit Limit, 
     Follow Ups,  Day-Bank-Cash book report, Tarcin, Tarcin accounting,
      tarcin accounting, v17 accounting,Tarcin Accounting, tarcin apps""",
    'author': 'Tarcin Robotic LLP',
    'company': 'Tarcin Robotic LLP',
    'maintainer': 'Tarcin Robotic LLP',
    'website': "https://tarcin.in",
    'depends': ['account', 'sale', 'account_check_printing',
                'base_account_budget', 'analytic'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/account_financial_report_data.xml',
        'data/cash_flow_data.xml',
        'data/followup_levels.xml',
        'data/multiple_invoice_data.xml',
        'data/recurring_entry_cron.xml',
        'data/account_pdc_data.xml',
        'views/reports_config_view.xml',
        'views/accounting_menu.xml',
        'views/account_group.xml',
        'views/credit_limit_view.xml',
        'views/account_configuration.xml',
        'views/res_config_view.xml',
        'views/account_followup.xml',
        'views/followup_report.xml',
        'wizard/asset_depreciation_confirmation_wizard_views.xml',
        'wizard/asset_modify_views.xml',
        'views/account_asset_views.xml',
        'views/account_move_views.xml',
        'views/product_template_views.xml',
        'views/multiple_invoice_layout_view.xml',
        'views/multiple_invoice_form.xml',
        'wizard/financial_report.xml',
        'wizard/general_ledger.xml',
        'wizard/partner_ledger.xml',
        'wizard/tax_report.xml',
        'wizard/trial_balance.xml',
        'wizard/aged_partner.xml',
        'wizard/journal_audit.xml',
        'wizard/cash_flow_report.xml',
        'wizard/account_bank_book_wizard_view.xml',
        'wizard/account_cash_book_wizard_view.xml',
        'wizard/account_day_book_wizard_view.xml',
        'report/report_financial.xml',
        'report/general_ledger_report.xml',
        'report/report_journal_audit.xml',
        'report/report_aged_partner.xml',
        'report/report_trial_balance.xml',
        'report/report_tax.xml',
        'report/report_partner_ledger.xml',
        'report/cash_flow_report.xml',
        'report/account_bank_book_view.xml',
        'report/account_cash_book_view.xml',
        'report/account_day_book_view.xml',
        'report/account_asset_report_views.xml',
        'report/report.xml',
        'report/multiple_invoice_layouts.xml',
        'report/multiple_invoice_report.xml',
        'views/recurring_payments_view.xml',
        'wizard/account_lock_date.xml',
        'views/account_payment_view.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    'application': True,
}

