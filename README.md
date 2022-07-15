KALPANA_COHORT CLASSIFICATION PROJECT

PROJECT GOALS
    - The goal of this project is to identify key drivers of the churn in Telco company, which customers are at risk of churn and make a recommendtaion for the change in order to retain more customers.
    - Build a classification model to predict the customer churn.

PROJECT DESCRIPTION
    The cost of acquiring a new customers can cost five times more than retaining the existing customers. US companies lose $136.8 billion per year due to avoidable consumer switching.The success rate of selling to an existing customer is around 60%-70%, while it is only at around (5-20) % with new customers. Due to these reasons retaining customers is just as important as, if not more important than, acquiring new ones. In this project different attributes(i.e features) of the customers will be analyzed to see if customers will indeed churn or not. A list of customers(.CSV) bound to churn will be created using the best performing machine learning model.

INITIAL KEY QUESTIONS
    1.Does internet service type plays a significant role in cutomer churning?
    2.Do customers with month to month contract type churn more?
    3.Does having tech support helps to ratain the customers?
    4.Does payment type determines how likely customers cancel the service?
    5.What role does tenure and monthly charges play on customers churning?

DATA DICTIONARY:
    
    Customer Id: Id specific to each customers

Some binary categorical attributes were encoded to numeric
    Churn: 0:No, 1:Yes
    Gender: 0:Male 1:Female
    Senior Citizen: 0: No 1: Yes
    Partner: 0:No, 1:Yes
    Dependents: 0:No, 1:Yes
    Phone_service: 0:No, 1:Yes
    paperless_billing: 0: No, 1: Yes
    churn: 0:No, 1:Yes
    

    Below data are encoded with dummy variables. While dummies were created  for the features with more than 2 subcategory.
        Contract_type: month to month, 1 year, 2 year
        Internet_service_type: DSL, Fiber Optic, None
        Multiple_lines: No, Yes, No Phone service
        Online_security: No, Yes, No Internet service
        Online_backup: No,yes,  No Internet service
        Device protection: No, yes,  No Internet service
        tech_support: No, Yes,  No Internet service
        streaming_tv:  No,  Yes, No Internet service
        streaming_movies: No, Yes, No Internet service
        payment_type: Mailed check,Electronic Check,  Creditcard(automatic), Bank transfer (automatic)

    All RANDOM STATES= 123
    Max depth for Decision Tree and Random Forest set to 6.

STEPS to Reproduce:
 In order to reproduce the final report and model you will need to follow process listed below.
    - env.py file that has credentials for successful connection with CodeUp DB Server. MySQL database contains the telco_churn data.
    - clone my project repo(including aquire.py and prepare.py).
    - libraries to be used are pandas, matplotlib, seaborn, numpy, sklearn
    - finally you should be able to run final_project report.

PLAN
    Create acquire and prepare module
        - these two are user defined functions for data acquisition and preparing a clean data.
        - acquire function is tested and added to acquire.py module.
        - codes to clean the acquire data along with dummies variables and function to split the clean data  were merged together and put in prepare.py module
        - There were no missing values in the dataset. total_charges column was change to correct datypes
        - unwanted columns or reduntant 
    
    Split Data
        prepared data was split into train, validate and test samples using the split function in prepare module. first the data was split into 80% as train_validate and 20% test. then train_validate(80%) was split into 80% train and 20% validate samples.

CONCLUSIONS
    The varibles with the highest correlation to whether a customer churns or not as per my exploration and analysisn were monthly_charges, tenure, internet service type, payment type,contract type, tech support. After examining the three different models for machine learning I found random forest with depth of 6 outperformed other two models. I chose accuracy as the metrics for the deciding best performaning  model. However, there exists future research with models that fit other classifications that werenot analysed in this project.


    