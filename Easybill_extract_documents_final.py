# Easybill Data Import Documents Info:
# Import useful libraries:
import os
import requests as re
from requests.auth import HTTPBasicAuth
import json
import pprint
import pandas as pd
from pandas.tseries.offsets import MonthEnd


# os.chdir(f"C:\Users\Abud Shalhoub\Documents\Python\Easybill_projects")

# set the API Key:
def update_easybill_documents():
    api_token = os.environ.get("easybill_api_key")

    headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token)}

    parameters = {'limit': '1000', 'page': 1}

    response = re.get('https://api.easybill.de/rest/v1/documents',
                    headers=headers, params=parameters).json()

    # to do:
    # define three lists which consist of lists of keys which have one value, keys which have dictronaries, keys which have list of dictionaries:
    key_include_dict = ['address', 'customer_snapshot',
                        'label_address', 'service_date']

    key_include_list_of_dict = ['items']

    columns_list = ['address', 'amount', 'amount_net', 'attachment_ids', 'bank_debit_form', 'billing_country', 'calc_vat_from', 'cancel_id', 'cash_allowance', 'cash_allowance_days', 'cash_allowance_text', 'contact_id', 'contact_label', 'contact_text', 'created_at', 'currency', 'customer_id', 'customer_snapshot', 'discount', 'discount_type', 'document_date', 'due_date', 'due_in_days', 'edited_at', 'external_id',
                    'fulfillment_country', 'grace_period', 'id', 'is_archive', 'is_draft', 'is_replica', 'items', 'label_address', 'last_postbox_id', 'login_id', 'number', 'order_number', 'paid_amount', 'paid_at', 'pdf_pages', 'pdf_template', 'project_id', 'ref_id', 'replica_url', 'service_date', 'shipping_country', 'status', 'text', 'text_prefix', 'text_tax', 'title', 'type', 'use_shipping_address', 'vat_country', 'vat_option']


    First_dataframe_keys = ['amount', 'amount_net', 'attachment_ids', 'bank_debit_form', 'billing_country', 'calc_vat_from', 'cancel_id', 'cash_allowance', 'cash_allowance_days', 'cash_allowance_text', 'contact_id', 'contact_label', 'contact_text', 'created_at', 'currency', 'customer_id', 'discount', 'discount_type', 'document_date', 'due_date', 'due_in_days', 'edited_at', 'external_id',
                            'fulfillment_country', 'grace_period', 'id', 'is_archive', 'is_draft', 'is_replica', 'last_postbox_id', 'login_id', 'number', 'order_number', 'paid_amount', 'paid_at', 'pdf_pages', 'pdf_template', 'project_id', 'ref_id', 'replica_url', 'shipping_country', 'status', 'text', 'text_prefix', 'text_tax', 'title', 'type', 'use_shipping_address', 'vat_country', 'vat_option']

    nested_dic = {"address": ['city', 'company_name', 'country', 'first_name', 'last_name', 'personal',
                            'salutation', 'state', 'street', 'suffix_1', 'suffix_2', 'title', 'zip_code'],
                "customer_snapshot": ['acquire_options', 'additional_groups_ids', 'bank_account', 'bank_account_owner', 'bank_bic', 'bank_code', 'bank_iban', 'bank_name', 'birth_date', 'cash_allowance', 'cash_allowance_days', 'cash_discount', 'cash_discount_type', 'city', 'company_name', 'country', 'court', 'court_registry_number', 'created_at', 'delivery_city', 'delivery_company_name', 'delivery_country', 'delivery_first_name', 'delivery_last_name', 'delivery_personal', 'delivery_salutation', 'delivery_state', 'delivery_street', 'delivery_suffix_1', 'delivery_suffix_2', 'delivery_title',
                                        'delivery_zip_code', 'display_name', 'document_pdf_type', 'due_in_days', 'emails', 'fax', 'first_name', 'grace_period', 'group_id', 'id', 'info_1', 'info_2', 'internet', 'last_name', 'login_id', 'mobile', 'note', 'number', 'payment_options', 'personal', 'phone_1', 'phone_2', 'postbox', 'postbox_city', 'postbox_country', 'postbox_state', 'postbox_zip_code', 'sale_price_level', 'salutation', 'sepa_agreement', 'sepa_agreement_date', 'since_date', 'state', 'street', 'suffix_1', 'suffix_2', 'tax_number', 'tax_options', 'title', 'updated_at', 'vat_identifier', 'zip_code'],
                "label_address": ['city', 'company_name', 'country', 'first_name', 'last_name',
                                    'personal', 'salutation', 'state', 'street', 'suffix_1', 'suffix_2', 'title', 'zip_code'],
                "service_date": ['type', 'date', 'date_from', 'date_to', 'text']

                }

    # loop over all pages and collect all values for the First Dataframe:
    First_dataframe_values = []
    for page_number in range(1, response['pages']+1):
        parameters['page'] = page_number
        response = re.get('https://api.easybill.de/rest/v1/documents',
                        headers=headers, params=parameters).json()
        for document in response['items']:
            for elem in First_dataframe_keys:
                if elem in document.keys():
                    First_dataframe_values.append(document[elem])
                else:
                    First_dataframe_values.append(None)


    First_dataframe_keys_adjusted_length = First_dataframe_keys * \
        len(First_dataframe_values)


    first_dictionary = {key: [] for key in First_dataframe_keys_adjusted_length}

    # loop to iterate through keys and values

    for key, val in zip(First_dataframe_keys_adjusted_length, First_dataframe_values):
        first_dictionary[key].append(val)

    first_dataframe = pd.DataFrame(first_dictionary)


    # loop over all pages and collect all values for the second Dataframe:

    second_dataframe_values = []

    for page_number in range(1, response['pages']+1):
        parameters['page'] = page_number
        response = re.get('https://api.easybill.de/rest/v1/documents',
                        headers=headers, params=parameters).json()
        for document in response['items']:  # loop over all the documents
            for k in nested_dic.keys():  # loop over al the keys in the
                if k in document.keys():
                    for elem in nested_dic[k]:
                        if elem in document[k].keys():
                            second_dataframe_values.append(document[k][elem])
                        else:
                            second_dataframe_values.append(None)
                else:
                    second_dataframe_values = second_dataframe_values + \
                        [None] * len(nested_dic[k])

    # create a List out of the dictionary values to merge it with the extracted list:

    second_dataframe_keys = []

    for k in nested_dic.keys():
        for item in nested_dic[k]:
            unique_value = k+"_"+item
            second_dataframe_keys.append(unique_value)

    second_dataframe_keys_adjusted_length = second_dataframe_keys * \
        len(second_dataframe_values)


    second_dictionary = {key: [] for key in second_dataframe_keys_adjusted_length}

    # loop to iterate through keys and values:

    for key, val in zip(second_dataframe_keys_adjusted_length, second_dataframe_values):
        second_dictionary[key].append(val)

    second_dataframe = pd.DataFrame(second_dictionary)

    # merge the two Dataframes:

    merged = pd.concat([first_dataframe, second_dataframe], axis=1)
    # delete empty columns:

    merged = merged.dropna(axis=1, how='all')

    # delete specific Columns:

    merged = merged.drop(columns=['attachment_ids', 'calc_vat_from', 'grace_period', 'is_archive', 'is_draft', 'is_replica', 'last_postbox_id', 'login_id', 'order_number', 'pdf_pages', 'text_prefix', 'text_tax', 'title', 'use_shipping_address', 'vat_country',
                                'text','address_personal', 'address_salutation', 'address_state', 'address_suffix_1', 'address_suffix_2',
                                'customer_snapshot_acquire_options', 'customer_snapshot_additional_groups_ids', 'customer_snapshot_cash_allowance_days', 'customer_snapshot_city', 'customer_snapshot_company_name', 'customer_snapshot_country', 'customer_snapshot_court_registry_number', 'customer_snapshot_created_at', 'customer_snapshot_delivery_city', 'customer_snapshot_delivery_company_name', 'customer_snapshot_delivery_country', 'customer_snapshot_delivery_first_name', 'customer_snapshot_delivery_last_name', 'customer_snapshot_delivery_personal', 'customer_snapshot_delivery_salutation', 'customer_snapshot_delivery_state', 'customer_snapshot_delivery_street', 'customer_snapshot_delivery_title', 'customer_snapshot_delivery_zip_code', 'customer_snapshot_display_name', 'customer_snapshot_document_pdf_type', 'customer_snapshot_due_in_days',
                                'customer_snapshot_first_name', 'customer_snapshot_grace_period', 'customer_snapshot_group_id',
                                'customer_snapshot_internet', 'customer_snapshot_last_name', 'customer_snapshot_login_id', 'customer_snapshot_mobile', 'customer_snapshot_number', 'customer_snapshot_personal', 'customer_snapshot_phone_1', 'customer_snapshot_postbox_city', 'customer_snapshot_postbox_country', 'customer_snapshot_postbox_state', 'customer_snapshot_postbox_zip_code', 'customer_snapshot_salutation',
                                'customer_snapshot_suffix_1', 'customer_snapshot_suffix_2',
                                'label_address_city', 'label_address_company_name', 'label_address_country', 'label_address_first_name', 'label_address_last_name', 'label_address_personal', 'label_address_salutation', 'label_address_state', 'label_address_street', 'label_address_title', 'label_address_zip_code',
                                'customer_snapshot_tax_number', 'customer_snapshot_since_date', 'customer_snapshot_state'
                                ])

    ### Define a function which converts Text to numbers:
    # merged = merged[merged['number'] != ['Reminder','Mahnung','Dunning']]

    # indexNames = merged[(merged['number'] == 'Dunning') & (merged['number'] == 'Mahnung') & (merged['number'] == '')].index


    # merged.drop(indexNames, inplace=True)




    'merged = merged.drop(index=to_drop)'



    def convert_to_num(data_frame,col):
        data_frame[col] = data_frame[col]/100    

    #### a list of items which should be converted to numbers:

    text_to_num_list = ['amount','amount_net','paid_amount']

    ##### Loop Over the Columns and convert them to numbers:

    for col in text_to_num_list:
        convert_to_num(merged,col)

    #  save the values into an excel File in the default directory:

    merged = merged[merged['amount'].notna()]
    merged = merged[merged['number'].notna()]

    ######### Convert to Date:

    merged['due_date']=pd.to_datetime(merged['due_date'],format='%Y-%m-%d')
    merged['document_date']=pd.to_datetime(merged['document_date'],format='%Y-%m-%d')
    merged['service_date_date_from']=pd.to_datetime(merged['service_date_date_from'],format='%Y-%m-%d')
    merged['service_date_date_to']=pd.to_datetime(merged['service_date_date_to'],format='%Y-%m-%d')
    merged['created_at']=pd.to_datetime(merged['created_at'],format='%Y-%m-%d')

    ##### Fill Out Empty Dates ######:
    for i in merged.index:
        if pd.isna(merged.loc[i,'service_date_text']) == False and merged.loc[i,'service_date_text'][0] =="%" and merged.loc[i,'number'] not in ('2021-11608','10156'):
            merged.loc[i,'service_date_text'] = merged.loc[i,'service_date_text'].strip(r"%laufzeit+monat%")
            merged.loc[i,'service_date_text'] = merged.loc[i,'service_date_text'].strip(r"-start% - %monat-end")
            merged.loc[i,'service_date_date_from'] =merged.loc[i,'document_date']
            merged.loc[i,'service_date_date_to'] =merged.loc[i,'document_date']  + MonthEnd(int(merged.loc[i,'service_date_text']))
            
        else:
            pass

    ######################################
    # add Month and Date Columns
    merged['Month_from'] = pd.DatetimeIndex(merged['service_date_date_from']).month
    merged['Year_from'] = pd.DatetimeIndex(merged['service_date_date_from']).year

    merged['Month_to'] = pd.DatetimeIndex(merged['service_date_date_to']).month
    merged['Year_to'] = pd.DatetimeIndex(merged['service_date_date_to']).year







    #######
    return merged.to_excel(r'C:\Users\Abud Shalhoub\Documents\Python\Documents.xlsx', index=False), merged.to_excel(r'C:\Users\Abud Shalhoub\OneDrive\OneDrive - RTB Technologies Pvt Ltd\Easybill_Report\Input\Documents\Documents.xlsx', index=False),print('######## DONE ########')

update_easybill_documents()