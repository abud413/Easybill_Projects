# Easybill Data Import Documents Info:
# Import useful libraries:
import os
import requests as re
from requests.auth import HTTPBasicAuth
import json
import pprint
import pandas as pd


api_token = os.environ.get("easybill_api_key")

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

data = {'address': {'city': '',
                    'company_name': '',
                    'country': '',
                    'first_name': None,
                    'last_name': None,
                    'personal': False,
                    'salutation': 0,
                    'state': '',
                    'street': '',
                    'suffix_1': None,
                    'suffix_2': None,
                    'title': None,
                    'zip_code': ''},
        'amount': 595000,
        'amount_net': 500000,
        'attachment_ids': [],
        'bank_debit_form': None,
        'billing_country': 'DE',
        'calc_vat_from': 0,
        'cancel_id': 390334864,
        'cash_allowance': None,
        'cash_allowance_days': None,
        'cash_allowance_text': None,
        'contact_id': None,
        'contact_label': None,
        'contact_text': None,
        'created_at': '2019-01-08 10:36:06',
        'currency': 'EUR',
        'customer_id': ,
        'customer_snapshot': {'acquire_options': 1,
                              'additional_groups_ids': [],
                              'bank_account': None,
                              'bank_account_owner': None,
                              'bank_bic': None,
                              'bank_code': None,
                              'bank_iban': None,
                              'bank_name': None,
                              'birth_date': None,
                              'cash_allowance': None,
                              'cash_allowance_days': 7,
                              'cash_discount': None,
                              'cash_discount_type': None,
                              'city': 'Hamburg',
                              'company_name': 'InnoGames GmbH',
                              'country': 'DE',
                              'court': None,
                              'court_registry_number': None,
                              'created_at': '2019-01-08',
                              'delivery_city': None,
                              'delivery_company_name': None,
                              'delivery_country': None,
                              'delivery_first_name': None,
                              'delivery_last_name': None,
                              'delivery_personal': False,
                              'delivery_salutation': 0,
                              'delivery_state': '',
                              'delivery_street': None,
                              'delivery_suffix_1': None,
                              'delivery_suffix_2': None,
                              'delivery_title': '',
                              'delivery_zip_code': None,
                              'display_name': 'InnoGames GmbH',
                              'document_pdf_type': 'default',
                              'due_in_days': None,
                              'emails': [],
                              'fax': None,
                              'first_name': None,
                              'grace_period': None,
                              'group_id': None,
                              'id': 275493439,
                              'info_1': None,
                              'info_2': None,
                              'internet': None,
                              'last_name': None,
                              'login_id': 163654,
                              'mobile': None,
                              'note': None,
                              'number': '10002',
                              'payment_options': None,
                              'personal': False,
                              'phone_1': None,
                              'phone_2': None,
                              'postbox': None,
                              'postbox_city': None,
                              'postbox_country': None,
                              'postbox_state': '',
                              'postbox_zip_code': None,
                              'sale_price_level': None,
                              'salutation': 0,
                              'sepa_agreement': None,
                              'sepa_agreement_date': None,
                              'sepa_mandate_reference': None,
                              'since_date': None,
                              'state': '',
                              'street': 'Friesenstraße 13',
                              'suffix_1': None,
                              'suffix_2': None,
                              'tax_number': None,
                              'tax_options': None,
                              'title': None,
                              'updated_at': '2019-01-08 10:35:03',
                              'vat_identifier': 'DE264068907',
                              'zip_code': '20097'},
        'discount': None,
        'discount_type': None,
        'document_date': '2019-01-08',
        'due_date': '2019-01-22',
        'due_in_days': 14,
        'edited_at': '2019-03-01 13:31:16',
        'external_id': None,
        'fulfillment_country': None,
        'grace_period': 14,
        'id': 349307299,
        'is_archive': False,
        'is_draft': True,
        'is_replica': False,
        'items': [{'booking_account': None,
                   'cost_price_charge': None,
                   'cost_price_charge_type': 'AMOUNT',
                   'cost_price_net': None,
                   'cost_price_total': None,
                   'description': 'Platform Fee',
                   'discount': None,
                   'discount_type': None,
                   'export_cost_1': None,
                   'export_cost_2': None,
                   'id': 671381394,
                   'item_type': 'PRODUCT',
                   'number': '1',
                   'position': 1,
                   'position_id': None,
                   'quantity': 1,
                   'quantity_str': '1',
                   'serial_number': None,
                   'serial_number_id': None,
                   'single_price_gross': 450000,
                   'single_price_net': 450000,
                   'total_price_gross': 4500,
                   'total_price_net': "",
                   'total_vat': "",
                   'type': 'POSITION',
                   'unit': None,
                   'vat_percent': 19},
                  {'booking_account': None,
                   'cost_price_charge': None,
                   'cost_price_charge_type': 'AMOUNT',
                   'cost_price_net': None,
                   'cost_price_total': None,
                   'description': 'Playable Ad Creation for FoE "Trading 2" (Table)',
                   'discount': None,
                   'discount_type': None,
                   'export_cost_1': None,
                   'export_cost_2': None,
                   'id': 671381964,
                   'item_type': 'PRODUCT',
                   'number': '2',
                   'position': 2,
                   'position_id': None,
                   'quantity': 1,
                   'quantity_str': '1',
                   'serial_number': None,
                   'serial_number_id': None,
                   'single_price_gross': 297500,
                   'single_price_net': 250000,
                   'total_price_gross': 297500,
                   'total_price_net': 250000,
                   'total_vat': 47500,
                   'type': 'POSITION',
                   'unit': None,
                   'vat_percent': 19}],
        'label_address': {'city': None,
                          'company_name': None,
                          'country': None,
                          'first_name': None,
                          'last_name': None,
                          'personal': False,
                          'salutation': 0,
                          'state': '',
                          'street': None,
                          'suffix_1': None,
                          'suffix_2': None,
                          'title': '',
                          'zip_code': None},
        'last_postbox_id': 240600324,
        'login_id': 163654,
        'number': '201910001',
        'order_number': '',
        'paid_amount': 0,
        'paid_at': None,
        'pdf_pages': 1,
        'pdf_template': 'EN',
        'project_id': None,
        'ref_id': None,
        'replica_url': None,
        'service_date': {'date': '2019-01-08',
                         'date_from': None,
                         'date_to': None,
                         'text': None,
                         'type': 'DEFAULT'},
        'shipping_country': None,
        'status': None,
        'text': 'Please remit the outstanding amount until&nbsp; '
        '%DOCUMENT.DUE-DATE%.<br>',
        'text_prefix': 'Dear Sir or Madam,<br>below we will charge you as discussed '
                'previously:<br>',
        'text_tax': None,
        'title': None,
        'type': 'INVOICE',
        'use_shipping_address': False,
        'vat_country': None,
        'vat_option': None}

response = re.post('https://api.easybill.de/rest/v1/documents',
                   headers=headers, json=data)

print(response.status_code)