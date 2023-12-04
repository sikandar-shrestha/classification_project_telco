
import pandas as pd
import env
import os



def check_file_exists(filename, query, url):
    '''
    This function caching the data.Either it from your local system or 
    from the codeup mysql database.
    
    '''
    if os.path.exists(filename):
        print('this file exists, reading csv')
        df = pd.read_csv(filename,index_col=0)
    else:
        print('this file doesnt exist, read from sql, and export to csv')
        df = pd.read_sql(query, url)
        df.to_csv(filename)
        
    return df






def get_telco_data():
    '''
    This function sets the filename to 'telco.csv', the url to read from the codeup mysql db 'telco_churn', 
    & the query to pull all data for the following left joined tables: customers, contract_types, internet_service_types, &    
    payment_type.
    It will then check if the file exists. If it does, it will read the file & return it to us as a dataframe. If it does not       exist, it will create the file & return it to us as a dataframe.
    '''
    url = env.get_db_url('telco_churn')
    query = '''
    select *
    from customers
        left join contract_types
            using (contract_type_id)
        left join internet_service_types
            using (internet_service_type_id)
        left join payment_types
            using (payment_type_id)
    '''
    
    filename = 'telco.csv'
    
    #call the check_file_exists fuction 
    df = check_file_exists(filename, query, url)
    return df

    return df