import pandas as pd
import acquire
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.2, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test





def prep_telco(df):
    '''This function cleans the telcho data by dropping unwanted columns and replacing some values in columns'''
    df= df.drop_duplicates()
    # Drop the unwanted columns
    df = df.drop(columns=['Unnamed: 0','contract_type_id','internet_service_type_id','payment_type_id'])
    
    #replace some values with 'No' in listed columns
    df.online_security = df['online_security'].str.replace('No internet service', 'No')
    df.online_backup = df['online_backup'].str.replace('No internet service', 'No')
    df.device_protection = df['device_protection'].str.replace('No internet service', 'No')

     # Convert to correct datatype
    df.total_charges = df['total_charges'].str.strip().replace('',0).astype(float)
    

    return df
    

    
def encode_telco(df):
#     Family describes the family type based on partners and dependents

    conditions_1 =[
        (df['partner']=='Yes')& (df['dependents']=='Yes'),
        (df['partner']=='Yes')& (df['dependents']=='No'),
        (df['partner']=='No')& (df['dependents']=='Yes'),
        (df['partner']=='No')& (df['dependents']=='No')]
    choices_1 = [0,1,2,3]
    df['family'] = np.select(conditions_1, choices_1)

#Phone services describes whether someone has a phone plan and whether or not they have multiple lines

    conditions_2 =[
        (df['phone_service']=='Yes')& (df['multiple_lines']=='Yes'),
        (df['phone_service']=='Yes')& (df['multiple_lines']=='No'),
        (df['phone_service']=='No')& (df['multiple_lines']== 'No')]
    choices_2 = [0,1,2]
    df['phone_services'] = np.select(conditions_2, choices_2)

#Streaming services describes what streaming services someone has.

    conditions_3 =[
        (df['streaming_tv']=='Yes')& (df['streaming_movies']=='Yes'),
        (df['streaming_tv']=='Yes')& (df['streaming_movies']=='No'),
        (df['streaming_tv']=='No')& (df['streaming_movies']=='Yes'),
        (df['streaming_tv']=='No')& (df['streaming_movies']=='No')]
    choices_3 = [0,1,2,3]
    df['streaming_services'] = np.select(conditions_3, choices_3)

#Online_services describes what types of online services someone has.

    conditions_4=[
        (df['online_security']=='Yes')& (df['online_backup']=='Yes'),
        (df['online_security']=='Yes')& (df['online_backup']=='No'),
        (df['online_security']=='No')& (df['online_backup']=='Yes'),
        (df['online_security']=='No')& (df['online_backup']=='No')]
    choices_4 = [0,1,2,3]
    df['online_services'] = np.select(conditions_4, choices_4)
    
    
    # encode binary categorical variables into numeric values
    df['e_device_protection'] = df['device_protection'].map({'Yes':1,'No':0,'No internet service':0})
    df['e_gender'] = df.gender.map({'Female': 1, 'Male': 0})
    df['e_paperless_billing'] = df.paperless_billing.map({'Yes':1, 'No':0})
    df['e_churn'] = df.churn.map({'Yes': 1, 'No': 0})
    df['etech_support']= df.tech_support.map({'Yes':1, 'No':0,'No internet service':0})
    df['e_internet_service']= df.internet_service_type.map({'None':0,'DSL':1, 'Fiber optic':2})
    df['e_payment']= df.payment_type.map({'Electronic check':0,'Mailed check':1,'Bank transfer (automatic)':2,'Credit card (automatic)':3 })
    df['e_contract']= df.contract_type.map({'One year':1,'Month-to-month':0, 'Two year':2 })

    encoded_df= df[['customer_id','e_churn','e_gender','senior_citizen','e_device_protection','e_paperless_billing','etech_support','e_internet_service','e_payment',
                    'e_contract','online_services','streaming_services','streaming_services','phone_services','family','monthly_charges','total_charges','tenure']]

    return encoded_df
