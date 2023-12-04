import pandas as pd






def preprocess_telco(train_df, val_df, test_df):
    '''
    preprocess_telco will take in three pandas dataframes
    of an acquired and prepared telco data set that has also been split into train, validate, and test.
    
    output:
    encoded, ML-ready versions of train, validate, and test with 
    object type columns encoded in the one-hot fashion
    return: (pd.DataFrame, pd.DataFrame, pd.DataFrame)
    '''
     
    encoding_vars = []
    # loop through the columns to fill encoded_vars with appropriate datatype 
    for col in train_df.columns:
        if train_df[col].dtype == 'O':
            encoding_vars.append(col)
    # initialize an empty list to hold our encoded dataframes:
    encoded_dfs = []
    for df in [train_df, val_df, test_df]:
        df_encoded_cats = pd.get_dummies(df[encoding_vars],drop_first=True).astype(int)
        encoded_dfs.append(pd.concat([df,df_encoded_cats],axis=1).drop(columns=encoding_vars))
    return encoded_dfs



