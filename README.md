# Student Performance Prediction

## Project Overview

The purpose of this project is to analyze and predict the academic performance of students using multiple linear regression techniques. The dataset used for this project contains various attributes that potentially influence student performance, such as demographic information, grades in previous subjects, and other relevant factors.

## Dataset

The dataset used in this project is the **Student Performance Dataset**, which can be found on [Kaggle](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression). This dataset includes:

- **Student Attributes**: Demographic information such as gender, age, and family background.
- **Academic Performance**: Grades from previous subjects and overall performance metrics.

### Data Fields

- `gender`: Gender of the student (male/female)
- `age`: Age of the student
- `address`: Address type (urban/rural)
- `family_size`: Size of the family
- `father_education`: Father's education level
- `mother_education`: Mother's education level
- `study_time`: Weekly study time
- `failures`: Number of past class failures
- `extracurricular_activities`: Participation in extracurricular activities
- `grades`: Final grades in various subjects

## Objective

The main objective of this project is to build a predictive model that can estimate student performance based on the provided features

## Methodology

1. **Data Preprocessing**: Cleaning the dataset, handling missing values, and encoding categorical variables.
2. **Exploratory Data Analysis (EDA)**: Visualizing relationships between features and student performance.
3. **Model Development**: Implementing multiple linear regression to predict academic performance.
4. **Model Evaluation**: Assessing the model's accuracy and performance using appropriate metrics.

## Requirements

To run this project, you'll need the following libraries:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
