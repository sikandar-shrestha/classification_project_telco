from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
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





      ################################## model evaluation on train and validate ##################################


def get_tree(X_train, X_validate, y_train, y_validate):
    '''get decision tree accuracy on train and validate data'''

    # create classifier object
    tree = DecisionTreeClassifier(max_depth=8, random_state=123)

    #fit model on training data
    tree.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Decision Tree on train data is {tree.score(X_train, y_train)}")
    print(f"Accuracy of Decision Tree on validate data is {tree.score(X_validate, y_validate)}")
    
    
    
    
    
def get_forest(X_train, X_validate, y_train, y_validate):
    '''get random forest accuracy on train and validate data'''

    # create model object and fit it to training data
    rf = RandomForestClassifier(min_samples_leaf=4,max_depth=6, random_state=123)
    rf.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(X_train, y_train)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(X_validate, y_validate)}")
    
    
    
    
def get_log_reg(X_train, X_validate, y_train, y_validate):
    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
    lr= LogisticRegression(solver='liblinear')
    lr.fit(X_train, y_train)

    # print result
    print(f"Accuracy of Logistic Regression on train is {lr.score(X_train, y_train)}")
    print(f"Accuracy of Logistic Regression on validate is {lr.score(X_validate, y_validate)}")
    
    
    
    ################################## model evaluation on test ############################################
    
    
    
# def get_log_reg_test(X_train, X_test, y_train, y_test):
#    '''get logistic regression accuracy on train and validate data'''

    # create model object and fit it to the training data
#    lr= LogisticRegression(solver='liblinear')
#    lr.fit(X_train, y_train)

    # print result
#    print(f"Accuracy of Logistic Regression on test is {lr.score(X_test, y_test)}")
    
    
    
    
    


    
    
    
    
    










