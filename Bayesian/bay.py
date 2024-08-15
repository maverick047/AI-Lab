import numpy as np
import pandas as pd
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

# Load and preprocess the dataset
heartDisease = pd.read_csv('C:\\Users\\91866\\OneDrive\\Desktop\\DS\\7.csv')
heartDisease.replace('?', np.nan, inplace=True)

# Display sample instances and attribute information
print('Sample instances from the dataset are given below:')
print(heartDisease.head())

print('\nAttributes and datatypes:')
print(heartDisease.dtypes)

# Define the Bayesian Network model
model = BayesianModel([
    ('age', 'heartdisease'),
    ('gender', 'heartdisease'),
    ('exang', 'heartdisease'),
    ('cp', 'heartdisease'),
    ('heartdisease', 'restecg'),
    ('heartdisease', 'chol')
])

# Learn the CPDs using Maximum Likelihood Estimator
print('\nLearning CPDs using Maximum Likelihood Estimators:')
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

# Perform inference with the Bayesian Network
inference = VariableElimination(model)

# Query and print the probability of HeartDisease given evidence
print('\n1. Probability of HeartDisease given evidence= restecg:')
print(inference.query(variables=['heartdisease'], evidence={'restecg': 1}))

print('\n2. Probability of HeartDisease given evidence= cp:')
print(inference.query(variables=['heartdisease'], evidence={'cp': 2}))
