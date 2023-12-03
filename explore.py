import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats




def cat_con_col(train):
    
    '''
    This function identifies categorical and continuous columns in a DataFrame.
    Input data: DataFrame
    Output:
    - cat_col: List of categorical columns
    - con_col: List of continuous columns
    '''
    
    cat_col = []
    con_col = []

    #looping through all columns
    for col in train.columns:
            #finding all my categorical columns by checking for how many unique values
            # if less than 100, append to cat_col
            if train[col].nunique() < 100:
                cat_col.append(col)
            else: 
                #if it has more than 100 unique values, append to continous column variable
                con_col.append(col)
                
                
    return cat_col,con_col








def explore_cat_target(train,columns_to_compare):
    
    target_variable='churn'
    # For loop to create contingency table and bar plot for each comparision column vs churn
    # describe and visualize the distribution of categorical variables and make inferences about 
    # the equality of proportions, independence of the variables, or agreement between variables.
    for column in columns_to_compare:


        # Create a contingency table
        contingency_table = pd.crosstab(train[column], train[target_variable])

        # Display the contingency table
        print(f"\nContingency Table for {column} vs. {target_variable}:\n")
        print(contingency_table)

        # To help visualize the contingency table, we can use a stacked bar plot
        contingency_table.plot.bar()
        plt.title(f'{column} vs. {target_variable}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()



def explore_con_target(train,con_col):
    
    target_variable='churn'
    # Create a for loop to compare each continuous variable to the target variable
    for column in con_col:
        # Visualize the distribution of the continuous variable 
        plt.figure(figsize=(10, 6))
        # Box plot with target variable and count
        sns.boxplot(x=target_variable, y=column, data=train)
        plt.title(f'{column} vs. {target_variable}')
        plt.xlabel(target_variable)
        plt.ylabel(column)
        plt.show()

    
    
                       
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








