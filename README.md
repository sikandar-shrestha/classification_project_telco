# Telco Customer Churn Classification Project

## Project Description
This project aims to predict customer churn for a Telco company by building a classification model using historical customer data. The goal is to identify factors influencing customer churn and create a predictive model that can forecast potential churners, allowing the company to take proactive retention measures.


## Initial Hypotheses and Questions

### Hypotheses:
    - There is relationship between 'payment_type' and 'churn'.
    - There is relationship between 'contract_type' and 'churn'.
    - monthly charges impacts significantly on 'churn'.
    - tenure has significantly related with 'churn'.

### Questions:
    - Does payment_type affect whether or not someone churned?
    - does contract type affect whether or not someone has churned?
    - Does monthly charges indicate whether or not someone churned?
    - Do many customers churn after a certain period?


## Data Dictionary

Here is a brief description of the features in the Telco dataset:
 
  
 
 | SN | Field Name | Description |
 | -- | ---------- | ----------- |   
 | 1. | customer_id | Unique identifier for each customer |
 | 2. | gender | Customer's gender (Male/Female) |
 | 3. | senior_citizen | Whether the customer is a senior citizen (1 for yes, 0 for no) |
 | 4. | partner | Whether the customer has a partner (Yes/No) |
 | 5. | dependents | Whether the customer has dependents (Yes/No) |
 | 6. | tenure | Number of months the customer has stayed with the company(1 to 72) |
 | 7. | phone_service | Whether a customer has a landline phone service (Yes/No) |
 | 8. | multiple_lines | Whether a customer has multiple lines of internet connectivity.(Yes/No/No phone service) |       
 | 9. | Online_security | Specifies if a customer has online security.(Yes/No/No internet sevice) |
 | 10. | online_backup| The type of internet services chosen by the customer.(Yes/No/No internet service) |
 | 11. | device_protection:| Specifies if a customer has opted for device protection.(Yes/No/No internet service) |  
 | 12. | tech_support| Whether a customer has opted for tech support of not.(Yes/No/No internet service) |      
 | 13. | streaming_tv | Whether a customer has an option of TV streaming.(Yes/No/No internet servie) |         
 | 14. | streaming_movies |   Whether a customer has an option of Movie streaming.(Yes/No/no internet service) |   
 | 15. | paperless_billing |  Whether a customer has opted for paperless billing.(Yes/No) |      
 | 16. | monthly_charges | Specifies the money paid by a customer each month. |   
 | 17. | total_charges| The total money paid by the customer to the company. |      
 | 18. | churn | This is the target variable which specifies if a customer has churned or not.(Yes/No) |                 
 | 19. | contract_type | The type of contract a customer has chosen.(one year/month-to-month/two year) |        
 | 20. | internet_service_type: | The type of internet services chosen by the customer.(DSL/fiber optic/neither) |
 | 21. |  payment_type | Specifies the method by which bills are paid.(bank transfer(automatic),credit card(automatic),electronic check, mailed check) |
                       
 
 
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

* To reproduce this project:

* Data: Obtain the Telco dataset from codeup mysql database named 'telco_churn'.

* Environment: Use Python 3.x (jupyter notebook)

* Code: Run the Jupyter Notebook Final_Report.ipynb inside my classification_project_telco repository.

* Instructions: Follow the comments and markdown cells in the notebook for step-by-step execution.



## Key Findings, Recommendations, & Takeaways

### Key Findings:

* The strongest relationship with churn are contract_type(month-to-month), payment_type(electronic     check),internet_service_type(Fiberoptic),tech_support(no),device_protection(no),online_backup(no),online_security(no),dependentrs(no),senior_citizen(0).

* Implement continuous improvements in service quality, network coverage, or additional features that align with customer preferences like payment_type, contract_type, online security, tech supports e.t.c.
 
* communication to address concerns and improve service quality.

### Recommendations:
* we might recommend and give attractive discount offer to customers for over a year, to prevent their churn rate is going high.

* Will need to investigate further asking are these fees associated with each payment type or what are their delivery speeds or how thes are conveience to make a payment.

* Identify high-risk tenure periods when churn rates tend to increase.Implement targeted retention campaigns during these phases, offering personalized support, exclusive benefits, or loyalty rewards to prevent churn.

* communication to address concerns and improve service quality.

* Implement continuous improvements in service quality, network coverage, or additional features that align with customer preferences like payment_type, contract_type, online security, tech supports e.t.c.




### Conclusion and Takeaways

* This project demonstrates the effectiveness of machine learning in predicting customer churn for Telco companies. 

* Understanding churn factors helps in making strategies to retain customers, thereby improving business sustainability.





























