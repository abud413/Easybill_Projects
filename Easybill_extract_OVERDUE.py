import pandas as pd
import os
import numpy as np
import datetime as dt

def overdue_update_sheet():
    data = pd.read_excel(r'\Users\Abud Shalhoub\Documents\Python\Documents.xlsx')

    data = data[data['cancel_id'].isna()]

    data = data[data['type'] == 'INVOICE']

    data = data[data['amount'] != 0]

    data = data[data['paid_amount'] == 0]

    data['due_date']=pd.to_datetime(data['due_date'],format='%Y-%m-%d')
    data['document_date']=pd.to_datetime(data['document_date'],format='%Y-%m-%d')
    data['service_date_date_from']=pd.to_datetime(data['service_date_date_from'],format='%Y-%m-%d')
    data['service_date_date_to']=pd.to_datetime(data['service_date_date_to'],format='%Y-%m-%d')
    data['created_at']=pd.to_datetime(data['created_at'],format='%Y-%m-%d')

    data = data[data['due_date'] <= dt.datetime.today()]

    data = data.drop(columns=['service_date_date','customer_snapshot_emails','billing_country','cancel_id','cash_allowance','cash_allowance_days','contact_id','discount','edited_at','id','paid_amount','paid_at','status','vat_option','address_city','address_country','address_first_name','address_last_name','address_street','address_zip_code','customer_snapshot_id','customer_snapshot_street','customer_snapshot_tax_options','customer_snapshot_updated_at','customer_snapshot_vat_identifier','customer_snapshot_zip_code','service_date_type'
    ])

    data = data[['number','address_company_name','customer_id','amount','amount_net','currency','created_at','document_date','due_date','due_in_days','type','service_date_date_from','service_date_date_to']]

    data = data.rename(columns={'number':'Invoice Number','address_company_name':'Customer','amount':'Invoice Amount'})

    return data.to_excel('OVERDUE.xlsx',index=False),data.to_excel(r'C:\Users\Abud Shalhoub\OneDrive\OneDrive - RTB Technologies Pvt Ltd\Easybill_Report\Input\Overdue\Overdue.xlsx', index=False)

overdue_update_sheet()

