## COVID-19-Data-Analysis-And-Prediction-Using-Machine-Learning

## Project Overview

Considering pandemic of COVID-19, data analysis and prediction 
seems promising to find-out useful information that can help to make decision on time 
for preventing spread of COVID-19. This project demonstrates the different analysis on 
confirmed/death/recovered case of COVID-19 and also the prediction on COVID-19 
confirmed case in Nepal. Data analysis was done over the global COVID-19 dataset and 
Nepal’s dataset. Data analysis shows, US possess top position in total confirmed and in 
total deaths but not in recovery. For predicting confirmed case of COVID-19, supervised 
machine learning algorithms such as linear regression (LR), random forest regression 
(RFR) and support vector regression (SVR) algorithms were tested. As a result, different 
conclusions were drawn through data analysis for controlling this pandemic and random 
forest regression performed the best among those three models for COVID-19 confirmed 
cases prediction with 99% accuracy on test set. Similarly, data visualization and the result 
of predictive model were deployed in the web.


## Objectives 

The primary objective of this project work is to provide valuable information that can 
help to control the wide-spread of COVID-19. This objective is divided into three blocks:
1. Extracting insight from COVID-19 dataset using data analysis and visualization 
technique.
2. Predicting future confirmed cases (applied only for Nepal) using machine 
learning.
3. Providing timely information using web-interface.

## Applications

As a result of data analysis and the deployment of predictive model, many hidden patterns 
within the COVID-19 dataset can be explored and the number of COVID-19 cases can 
be predicted. By this, the probable casual factors can be explored out and the control 
strategies can be designed to control them. Furthermore, after knowing the number of 
cases and the probable number of cases of a particular area, the contact tracing and PCR 
test can be done accordingly. Even the highly infected regions can be sealed so that 
further spread is controlled. In addition to this, the project will also help in distribution 
of vaccines. The countries with higher prevalence rate and incidence rate will be 
prioritized for vaccination. Furthermore, the project will explore the specific factors that 
are associated with COVID-19 transmission. So, it will help different nations, 
organizations, individuals in designing control strategies and budgeting so that it can be 
controlled effectively.


## Dataset

We used secondary data collection method for this project. Global COVID-19 dataset 
provided by Johns Hopkins University which was in CSV format was imported.


## Future Enhancement

Our final model faces the problem of over-fitting. There were some inappropriate data in the dataset which was in contrast. Existence of such data skewed our dataset and removal of such data decreased 
the volume of dataset which was the main reason behind overfitting.
So, as a future work to clear up the problem of overfitting, we can add more data to the 
algorithm so that the model will generalize well. Moreover, early stopping, fine-tuning 
the model and using other optimization algorithms may resolve the problem of overfitting
as to predict more accurately.


## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Aryal-Rupesh/COVID-19-Data-Analysis-And-Prediction-Using-Machine-Learning.git  


## Example usage
```bash 
python app.py
```
We welcome contributions to this project. To contribute, follow these steps:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes
Submit a pull request


