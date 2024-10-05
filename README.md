# Student Performance Prediction

## Project Objective

The objective of this project is to predict students' academic performance based on various factors influencing their educational outcomes. The analysis utilizes data on study hours, previous scores, extracurricular activities, sleep hours, and the number of sample question papers practiced. The purpose of this project is to analyze and predict the academic performance of students using multiple linear regression techniques. The dataset used for this project contains various attributes that potentially influence student performance, such as demographic information, grades in previous subjects, and other relevant factors.

## Used Variables

The following variables were utilized in the project:

- **Hours Studied**: The number of hours students dedicate to studying.
- **Previous Scores**: Students' scores from earlier exams or tests.
- **Extracurricular Activities**: Students' participation in extracurricular activities that may affect their study time.
- **Sleep Hours**: The average number of hours of sleep per day, which can influence concentration and academic performance.
- **Sample Question Papers Practiced**: The number of practice papers that students worked on before exams.
- **Performance Index**: An index representing the overall score of the student.

## Used Evaluation Metrics
- **Accuracy:** The ratio of correctly classified samples to the total number of samples, indicating the model's overall effectiveness.
- **Precision:** Measures the accuracy in identifying positive examples, calculated as true positives divided by the total of true positives and false positives.
- **Recall:** Indicates how well the model identifies all positive samples, computed as true positives divided by the total of true positives and false negatives.
- **F1 Score**: The harmonic mean of precision and recall, providing a balance between the two metrics, especially in imbalanced datasets.

## Scatter Plot of Model Predictions
https://github.com/kizokubanczyk/student_Performance/blob/main/scores/LinearRegression_plot.png

## Requirements

To run the project, the following libraries are required:
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
