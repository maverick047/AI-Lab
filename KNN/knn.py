import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Define column names
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# Read dataset into a pandas DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Define features and target variable
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Print the first few rows of the features
print(X.head())

# Split the data into training and testing sets
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.10)

# Create and train the k-NN classifier
classifier = KNeighborsClassifier(n_neighbors=5).fit(Xtrain, ytrain)

# Make predictions
ypred = classifier.predict(Xtest)

# Print results
print("\n-------------------------------------------------------------------------")
print('{:<25} {:<25} {:<25}'.format('Original Label', 'Predicted Label', 'Correct/Wrong'))
print("-------------------------------------------------------------------------")

for i, label in enumerate(ytest):
    print('{:<25} {:<25}'.format(label, ypred[i]), end="")
    if label == ypred[i]:
        print(' {:<25}'.format('Correct'))
    else:
        print(' {:<25}'.format('Wrong'))

print("-------------------------------------------------------------------------")

# Print confusion matrix
print("\nConfusion Matrix:\n", metrics.confusion_matrix(ytest, ypred))
print("-------------------------------------------------------------------------")

# Print classification report
print("\nClassification Report:\n", metrics.classification_report(ytest, ypred))
print("-------------------------------------------------------------------------")

# Print accuracy score
print('Accuracy of the classifier is %0.2f' % metrics.accuracy_score(ytest, ypred))
print("-------------------------------------------------------------------------")
