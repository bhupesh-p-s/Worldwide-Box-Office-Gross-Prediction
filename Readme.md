# WORLDWIDE BOX OFFICE GROSS PREDICTION

## Introduction
This project uses machine learning techniques to predict the worldwide box office gross of a movie, based on various features such as genre, director, and stars.

## Prerequisites
The following packages are required to run this project:
* pandas
* numpy
* matplotlib
* seaborn
* sklearn
* requests
* beautifulsoup4

## Data Collection
The data for this project was collected from the IMDb website using web scraping techniques with the requests and Beautiful Soup libraries.

## Data Cleaning and Engineering
Before modeling, the collected data underwent a process of cleaning and engineering to prepare it for analysis. This involved dealing with missing values, converting data into the correct format, and creating new features through one-hot encoding.

## Machine Learning
Three machine learning models were used in this project: 
* Random Forest Regressor
* Gradient Boosting Regressor
* Support Vector Regression (SVR)

The model with the highest accuracy was found to be Gradient Boosting Regressor and was used for the final prediction.

## Conclusion
This project demonstrates the use of machine learning techniques to predict the worldwide box office gross of a movie based on various features. The Random Forest Regressor model was found to be the most efficient and accurate for this prediction task.


