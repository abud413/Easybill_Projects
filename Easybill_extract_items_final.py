# Easybill Data Import Documents Info:
# Import useful libraries:
import os
import requests as re
from requests.auth import HTTPBasicAuth
import json
import pprint
import pandas as pd

# set the API Key:

def update_easybill_items():
    api_token = os.environ.get("easybill_api_key")

    headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token)}

    parameters = {'limit': '1000', 'page': 1}

    response = re.get('https://api.easybill.de/rest/v1/documents',
                    headers=headers, params=parameters).json()

    items_keys = ['booking_account', 'cost_price_charge', 'cost_price_charge_type', 'cost_price_net', 'cost_price_total', 'description', 'discount', 'discount_type', 'export_cost_1', 'export_cost_2', 'id', 'item_type', 'number',
                'position', 'position_id', 'quantity', 'quantity_str', 'serial_number', 'serial_number_id', 'single_price_gross', 'single_price_net', 'total_price_gross', 'total_price_net', 'total_vat', 'type', 'unit', 'vat_percent']

    additional = ['number','type','address_company_name']

    final_dict = ['booking_account', 'cost_price_charge', 'cost_price_charge_type', 'cost_price_net', 'cost_price_total', 'description', 'discount', 'discount_type', 'export_cost_1', 'export_cost_2', 'id', 'item_type', 'number',
                'position', 'position_id', 'quantity', 'quantity_str', 'serial_number', 'serial_number_id', 'single_price_gross', 'single_price_net', 'total_price_gross', 'total_price_net', 'total_vat', 'type', 'unit', 'vat_percent','document_number']
    v = []

    for page_number in range(1, response['pages']+1):
        parameters['page'] = page_number
        response = re.get('https://api.easybill.de/rest/v1/documents',
                        headers=headers, params=parameters).json()

        for document in response['items']: # go Through all the documents in the response Page
            if 'items' in document.keys(): # after that check whether each document has the Item element which contains the info
                for f in document['items']: # If Item exists, then loop theough each list of the two or more lists in the Item
                    for elem in items_keys: # check wether each element in the pre-defined dictionary is in each list 
                        if elem in f.keys():
                            v.append(f[elem])

                        elif elem not in f.keys():
                            v.append(None)
                        else:
                            pass
                    v.append(document['number'])
            else:
                pass




    items_keys_adjusted_length = final_dict * int((len(v)/28))

    # print(len(items_keys_adjusted_length))

    dictionary = {key: [] for key in items_keys_adjusted_length}

    # print(dictionary)

    # # loop to iterate through keys and values:

    for key, val in zip(items_keys_adjusted_length, v):
        dictionary[key].append(val)

    Items_df = pd.DataFrame(dictionary)

    droped_columns = ['booking_account', 'cost_price_charge','discount', 'discount_type', 'export_cost_1', 'export_cost_2','serial_number', 'serial_number_id', 'unit' ]

    Items_df = Items_df.drop(columns=droped_columns)

    Price_columns = ['single_price_gross', 'single_price_net', 'total_price_gross', 'total_price_net', 'total_vat']

    for PRICE_ITEM in Price_columns:
        Items_df[PRICE_ITEM] = Items_df[PRICE_ITEM]/100


    return Items_df.to_excel('items.xlsx',index=False),Items_df.to_excel(r'C:\Users\Abud Shalhoub\OneDrive\OneDrive - RTB Technologies Pvt Ltd\Easybill_Report\Input\Items\items.xlsx',index=False),print('######## DONE ########')


update_easybill_items()

#### exratct_it_as DF only :

def update_easybill_items_DF():
    api_token = os.environ.get("easybill_api_key")

    headers = {'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token)}

    parameters = {'limit': '1000', 'page': 1}

    response = re.get('https://api.easybill.de/rest/v1/documents',
                    headers=headers, params=parameters).json()

    items_keys = ['booking_account', 'cost_price_charge', 'cost_price_charge_type', 'cost_price_net', 'cost_price_total', 'description', 'discount', 'discount_type', 'export_cost_1', 'export_cost_2', 'id', 'item_type', 'number',
                'position', 'position_id', 'quantity', 'quantity_str', 'serial_number', 'serial_number_id', 'single_price_gross', 'single_price_net', 'total_price_gross', 'total_price_net', 'total_vat', 'type', 'unit', 'vat_percent']

    additional = ['number','type','address_company_name']

    final_dict = ['booking_account', 'cost_price_charge', 'cost_price_charge_type', 'cost_price_net', 'cost_price_total', 'description', 'discount', 'discount_type', 'export_cost_1', 'export_cost_2', 'id', 'item_type', 'number',
                'position', 'position_id', 'quantity', 'quantity_str', 'serial_number', 'serial_number_id', 'single_price_gross', 'single_price_net', 'total_price_gross', 'total_price_net', 'total_vat', 'type', 'unit', 'vat_percent','document_number']
    v = []

    for page_number in range(1, response['pages']+1):
        parameters['page'] = page_number
        response = re.get('https://api.easybill.de/rest/v1/documents',
                        headers=headers, params=parameters).json()

        for document in response['items']: # go Through all the documents in the response Page
            if 'items' in document.keys(): # after that check whether each document has the Item element which contains the info
                for f in document['items']: # If Item exists, then loop theough each list of the two or more lists in the Item
                    for elem in items_keys: # check wether each element in the pre-defined dictionary is in each list 
                        if elem in f.keys():
                            v.append(f[elem])

                        elif elem not in f.keys():
                            v.append(None)
                        else:
                            pass
                    v.append(document['number'])
            else:
                pass




    items_keys_adjusted_length = final_dict * int((len(v)/28))

    # print(len(items_keys_adjusted_length))

    dictionary = {key: [] for key in items_keys_adjusted_length}

    # print(dictionary)

    # # loop to iterate through keys and values:

    for key, val in zip(items_keys_adjusted_length, v):
        dictionary[key].append(val)

    Items_df = pd.DataFrame(dictionary)

    droped_columns = ['booking_account', 'cost_price_charge','discount', 'discount_type', 'export_cost_1', 'export_cost_2','serial_number', 'serial_number_id', 'unit' ]

    Items_df = Items_df.drop(columns=droped_columns)

    Price_columns = ['single_price_gross', 'single_price_net', 'total_price_gross', 'total_price_net', 'total_vat']

    for PRICE_ITEM in Price_columns:
        Items_df[PRICE_ITEM] = Items_df[PRICE_ITEM]/100


    return Items_df

update_easybill_items_DF()
