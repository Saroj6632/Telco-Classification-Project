import pandas as pd
import env
import os




''' function to connect to CodeUp SQL database'''
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{db}'



def new_telco_data():
    ''' this function  runs the SQL querry to connect to telcho database  and get all the columns  and returns as a dataframe'''
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df








def get_telco_data():
    '''this function returns the telcho data and creates the csv file in local directory  if it doesnot exist already.'''
    filename= "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read data from database in dataframe
        df= new_telco_data()
        #cache data
        df.to_csv(filename)
        return df



