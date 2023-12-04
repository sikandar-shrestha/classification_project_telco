# Telco Customer Churn Classification Project

## Project Description
This project aims to predict customer churn for a Telco company by building a classification model using historical customer data. The goal is to identify factors influencing customer churn and create a predictive model that can forecast potential churners, allowing the company to take proactive retention measures.


## Initial Hypotheses and Questions

### Hypotheses:
    - Customers with longer tenure are less likely to churn.
    - Customers with more additional services (e.g., online security, tech support) are less likely to churn.
    - Contract type may significantly impact churn rates.

### Questions:
    - What are the primary factors contributing to customer churn?
    - Can the company predict potential churners accurately?


## Data Dictionary

Here is a brief description of the features in the Telco dataset:
   1.|  customer_id|       Unique identifier for each customer|
   2.|  gender|            Customer's gender (Male/Female)|
   3.|  senior_citizen|    Whether the customer is a senior citizen (1 for yes, 0 for no)|
   4.|  partner:|           Whether the customer has a partner (Yes/No)|
   5.|  dependents:|        Whether the customer has dependents (Yes/No)|
   6.|  tenure:|            Number of months the customer has stayed with the company(1 to 72)|
   7.| phone_service :|    Whether a customer has a landline phone service (Yes/No)|
   8.|  multiple_lines :|   Whether a customer has multiple lines of internet connectivity.(Yes/No/No phone service)|       
   9.|  Online_security:|   Specifies if a customer has online security.(Yes/No)|
  10.|  online_backup :|    The type of internet services chosen by the customer.(Yes/No)|
  11.|  device_protection:| Specifies if a customer has opted for device protection.(Yes/No) |  
  12.|  tech_support  :|    Whether a customer has opted for tech support of not.(Yes/No)|      
  13.|  streaming_tv :|     Whether a customer has an option of TV streaming.(Yes/No) |         
  14.|  streaming_movies :| Whether a customer has an option of Movie streaming.(Yes/No/no internet service)|   
  15.|  paperless_billing :|Whether a customer has opted for paperless billing.(Yes/No)|      
  16.|  monthly_charges :|  Specifies the money paid by a customer each month.|   
  17.|  total_charges :|    The total money paid by the customer to the company.|      
  18.|  churn :|            This is the target variable which specifies if a customer has churned or not.(Yes/No)|                 19.|  contract_type:|     The type of contract a customer has chosen.(one year/month-to-month/two year)|        
  20.|  internet_service_type:|  The type of internet services chosen by the customer.(DSL/fiber optic/neither)|
  21.|  payment_type :|  Specifies the method by which bills are paid.
                       (bank transfer(automatic),credit card(automatic),electronic check, mailed check)|
                       
 
 
 ## Project Planning
1. Plan:telco's customer info analyze and studying different features effects on churned customer.  
2. Data Acquire: Obtain the Telco dataset from the company's database or source.
3. Data Cleaning: Handle missing values, outliers, and inconsistencies in the dataset.
4. Exploratory Data Analysis (EDA): Explore relationships between features, visualize distributions, and analyze correlations.
5. Feature Engineering/Preprocessing: Transform categorical variables, handle scaling, and prepare features for modeling.
6. Model Building: Train classification models like Logistic Regression, Random Forest, KNN
7. Model Evaluation: Assess model performance using appropriate metrics like accuracy, precision, recall, etc.
8. Model Optimization: Tune hyperparameters and perform feature selection to improve model performance.
9. Final Evaluation and Interpretation: Choose the best model, evaluate on test data, and interpret key findings.
10.Product delivery: present the findings and recommendations.




## Reproducibility
To reproduce this project:
Data: Obtain the Telco dataset from [source link].
Environment: Use Python 3.x with required libraries listed in requirements.txt.
Code: Run the Jupyter Notebook Telco_Churn_Classification.ipynb.
Instructions: Follow the comments and markdown cells in the notebook for step-by-step execution.



## Key Findings, Recommendations, & Takeaways

### Key Findings:
- The strongest relations of churn are contract_type(month-to-month), payment_type(electronic     check),internet_service_type(Fiberoptic),tech_support(no),device_protection(no),online_backup(no),online_security(no),dependentrs(no),senior_citizen(0)

- Model decision tree(algorithm) with depth=8 achieves the highest accuracy.


### Recommendations:
- Focus on retaining customers with long tenure by offering loyalty rewards or discounts.
- Improve service quality in areas identified as significant churn predictors.


### Conclusion and Takeaways
- This project demonstrates the effectiveness of machine learning in predicting customer churn for Telco companies. 

- Understanding churn factors helps in making strategies to retain customers, thereby improving business sustainability.





























