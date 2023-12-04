
from sklearn.model_selection import train_test_split




    
    

    
def prep_telco(df):
    
    
    """
    function named prep_telco that accepts the raw telco dataframe, 
    and returns the data with the transformations.

    """
    # Drop any unnecessary, unhelpful, or duplicated columns.
    df = df.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0.0')
    df['total_charges']=df['total_charges'].astype('float')
    df['internet_service_type']=df['internet_service_type'].fillna('neither')
    # set the index
    df=df.set_index('customer_id')
    return df


    

    
def splitting_data(df,target):
    
    """
    This function takes in any DataFrame and a target variable as an argument 
    and returns train, validate, and test variables stratifying on the target variable.
    It returns these variables as DataFrames with a printout of their proportion to the original DataFrame.
    
    """

    # 1st split
    #this is return two dataframes
    train,validate_test=train_test_split(df, #send in initial df
                                train_size=0.60, #size of the train df, and the test size will default to 1-train_size
                                random_state=123, #set any number here for consistency
                                stratify=df[target] #need to stratify on target variable
                                                 ) 
            
            
            
     # 2nd split
    validate,test=train_test_split(validate_test,
                                           train_size=0.5,
                                           random_state=123,
                                           stratify=validate_test[target]
                                          )
            
            
    return train, validate, test
        
        
        
        
        
        
        
        
        