import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')

# Update sex column to numerical, 1 = female, 0 = male
passengers['Sex'] = passengers['Sex'].map({'female': 1, 'male': 0})

# Fill the nan values in the age column with average mean
passengers.fillna(value={
'Age': passengers['Age'].mean()
}, inplace=True)

# Create a first class column, 1 = first class
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)

# Create a second class column, 1 = second class
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)

# Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survival = passengers['Survived']

# Perform train, test, split
x_train, x_test, y_train, y_test = train_test_split(features, survival, test_size=0.2)

# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(x_train, y_train)

# Score the model on the train data
training_score = model.score(x_train, y_train)
print('Training score: ' + str(training_score))

# Score the model on the test data
test_score = model.score(x_test, y_test)
print('Test score: ' + str(test_score))

# Analyze the coefficients
print('Model coefficients:')
coef_list = list(zip(['Sex', 'Age', 'FirstClass', 'SecondClass'], model.coef_[0]))
for coef in coef_list:
  print(coef[0] + ': ' + str(coef[1]))

# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
Myself = np.array([0.0,24.0,0.0,1.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, Myself])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)

# Make survival predictions
sample_predictions = model.predict(sample_passengers)
for name, prediction in list(zip(['Jack', 'Rose', 'Myself'], sample_predictions)):
  if prediction == 1:
    print(name + ': will survive')
  else:
    print(name + ': will not survive')
