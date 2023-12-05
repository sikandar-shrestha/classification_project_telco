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



def cat_not_churn(cat_col):
    '''
    Input: categorical columns
    ouput: categorical columns list without churn column
    
    '''
    
    # Target variable is churn
    target_variable = 'churn'

    # Initialize an empty list to store columns for comparison
    columns_to_compare = []

    # Create a for loop to iterate through each column in the categorical column list
    # appending our comparision list as long as the column is not churn
    for column in cat_col:
        if column != target_variable:
            columns_to_compare.append(column)
    else:
        pass
    
    return columns_to_compare








def explore_cat_target(train,columns_to_compare):
    
    '''
    input: train dataset and columns_to_compare
    
    output: distplays all barplot list between columns_to_compare vs target 
    
    '''
    
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
    
    '''
    input: train and continuous columns
    
    output: boxplot 
    
    '''
    
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
        
        
        
def bar_pay_tar(train):
    '''
    This function shows the relationship between 
    payment_type Vs churn.
    
    input : train dataframe
    
    output : barplot diagram
    
    '''
    
    # customers with electronic check payment types churned a lot
    plt.figure(figsize=(10, 6))
    sns. countplot(data=train,x='payment_type', hue='churn' )
    plt.title('Churn by Payment Type')
    plt.xlabel('Payment Type')
    plt.ylabel('Count')
    plt.show()
    
    
    
def chi_pay_tar(train):
    
    '''get result of chi-square for payment_type and chrn'''
    
    observed = pd.crosstab(train.payment_type, train.churn)

    chi2, p, dof, expected = stats.chi2_contingency(observed)

    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

    

 
 
    
    
def pie_contract_tar(train):
    
    '''
    This function shows the relationship between 
    contract_type Vs churn.
    
    input : train dataframe
    
    output : pie chart
    
    '''
    # create axes objects
    fig,(ax1,ax2,ax3) = plt.subplots(1,3,figsize=(10,10))

    # generate pie chart and assign it to ax1
    values = [len(train.churn[(train.contract_type == 'Month-to-month') & (train.churn == 'Yes')]),
              len(train.churn[(train.contract_type == 'Month-to-month') & (train.churn == 'No')])]
    labels = ['churn', 'no churn']

    ax1.pie(values, labels=labels,autopct='%.0f%%', colors=['green', 'yellow'])
    ax1.title.set_text('churn by Month-to-month')
    
    
    # generate pie chart and assign it to ax2
    values = [len(train.churn[(train.contract_type == 'Two year') & (train.churn == 'Yes')]),
              len(train.churn[(train.contract_type == 'Two year') & (train.churn == 'No')])]
    labels = ['churn', 'no churn']

    ax2.pie(values, labels=labels,autopct='%.0f%%',colors=['cyan', 'pink'])
    ax2.title.set_text('churn by Two year')
    
    
    
    # generate pie chart and assign it to ax3
    values = [len(train.churn[(train.contract_type == 'One year') & (train.churn == 'Yes')]),
              len(train.churn[(train.contract_type == 'One year') & (train.churn == 'No')])]
    labels = ['churn', 'no churn']

    ax3.pie(values, labels=labels, autopct='%.0f%%', colors=['#ffc3a0', '#c0d6e4'])
    ax3.title.set_text('churn by One year')
    
    
    # display plot
    plt.tight_layout
    plt.show()

    
    
    
    
    
    
def chi_contract_tar(train):
    
    
    '''get result of chi-square for contract_type and churn'''
    
    observed = pd.crosstab(train.contract_type, train.churn)

    chi2, p, dof, expected = stats.chi2_contingency(observed)

    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')
    
    
    
    
def get_mann_whitney(train):
    
    '''
    input: train dataset
    
    output: mannwhitneyu statistics and p value
    
    '''
    
    #make two arrays of peoples for churned and not churned

    #all the fares for people that survived
    churned = train[train.churn == 'Yes'].monthly_charges

    #all the fares for people that didnt survive
    not_churned = train[train.churn == 'No'].monthly_charges
    
    
    # Performing a mann-whitney

    stat, p_value = stats.mannwhitneyu(churned,not_churned)
    print(f'stat:{stat}')
    print(f'p_value:{p_value}')
    
    
    
    
def chi_tenure_tar(train):
    '''
       This function gives the chi^2 statistic and p_value
       input: train dataset
       output: chi^2-stats
    
    '''
    
    
    # Create bins for tenure in terms of years
    bins = [0, 12, 24, 36, 48, 60, 72, 84]  # adjust as needed

    # Create labels for the bins (representing years)
    labels = ['0', '1', '2', '3', '4', '5', '6']

    # Bin the 'tenure' column
    train['tenure_years'] = pd.cut(train['tenure'], bins=bins, labels=labels, right=False)

    # Display the DataFrame with the new 'tenure_years' column
    print(train[['tenure', 'tenure_years']])
    
    
    # contingency table:
    observed_tenure = pd.crosstab(train.churn, train.tenure_years)
    chi2, p, dof, expected = stats.chi2_contingency(observed_tenure)
    
    # print contingency table
    print(observed_tenure)
    
    #output values
    print('Observed')
    print(observed_tenure.values)
    print('\nExpected')
    print(expected.astype(int))
    print('\n----')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')



    
    
    

    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    



        
        
        


    
    
                       
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








