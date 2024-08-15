import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 
# importing the dataset 
dataset = pd.read_csv("C:\\Users\\91866\\OneDrive\\Desktop\\DS\\5.csv") 
# split the data into inputs and outputs 
X = dataset.iloc[:, [0,1]].values 
y = dataset.iloc[:, 2].values 
# training and testing data 
from sklearn.model_selection import train_test_split 
# assign test data size 25% 
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size= 0.25, random_state=0) 
# importing standard scaler 
from sklearn.preprocessing import StandardScaler 
# scalling the input data 
sc_X = StandardScaler()  
X_train = sc_X.fit_transform(X_train) 
X_test = sc_X.fit_transform(X_test) 
# importing classifier 
from sklearn.naive_bayes import BernoulliNB 
# import Gaussian Naive Bayes classifier 
from sklearn.naive_bayes import GaussianNB 
# create a Gaussian Classifier 
classifer1 = GaussianNB() 
# training the model 
classifer1.fit(X_train, y_train) 
# testing the model 
y_pred1 = classifer1.predict(X_test) 
# importing accuracy score 
from sklearn.metrics import accuracy_score 
# printing the accuracy of the model 
print(accuracy_score(y_test,y_pred1))
