# Project Proposal

## What is the problem that you will be investigating?
 
Predicting the presence or absence of cardiovascular disease, given 11 input features comprising of
- general information about the patient (age, height, weight, sex)
- a medical examination (systolic/diastolic blood pressure, cholesterol/glucose levels) 
- and an assessment of contributing habits (smoking, alcohol, physical activity)
 
 
## Why is it interesting?
 
It may assist general practitioners in diagnosing cardiovascular disease. This disease is a leading cause of death and many are preventable. The Machine Learning model might therefore be a useful tool to bring attention to early stages and to minimize examination mistakes by providing a second opinion. Of course, doctors should never solely rely on machine learning predictions, rather than see them as a self-checking-system. Further examination by a cardiologist should always be considered.
 
## What reading will you examine to provide context and background?
 
Cardiovascular diseases in general. 

Other applications of machine learning models in the medical field.
 

## What data will you use? If you are collecting new data, how will you do it?
 
We will be using a dataset found on kaggle consisting of 70000 labelled patient records: https://www.kaggle.com/sulianova/cardiovascular-disease-dataset 

Unfortunately, as pointed out by other users on kaggle, the original source of this dataset is unclear. However, we believe that for our purposes, this dataset is adequate.
 
 
## What method or algorithm are you proposing?
 
We will be using Linear Classification with a kernel function and some sort of regularization.
 
 
## How will you evaluate your results? Qualitatively, what kind of results do you expect (e.g. plots or figures)?
 
We expect our model to learn to classify the presence or absence of cardiovascular disease and output its corresponding confidence probabilities. Of course, we don't want our model to learn inputs and corresponding labels by heart, so we will use _cross-validation_ to ensure that the model generalizes well. 

We will plot the training/generalization loss over time and we will visualize the prediction clusters using scatter plots (pair plots? possibly by using multiple dimensions?).

## Quantitatively, what kind of analysis will you use to evaluate and/or compare your results (e.g. what performance metrics or statistical tests)?
 
We will classify our results into true-positives, false-positives, true-negatives und false-negatives. Various key figures can be calculated from this, which in turn indicate the model's robustness (confusion matrix). We will evaluate the quality of our model using the _Receiver Operating Characteristic Curve_ and _F1 Score_ (Precision & Recall).
