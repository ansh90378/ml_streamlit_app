import pandas as pd
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv('data/iris.csv')
print(data.head())

# map species to numerical values
data['species'] = data['species'].map({
    'setosa': 0,
    'versicolor':1,
    'virginica':2
})

print(data.species.value_counts())

# define features and labels
X = data.drop('species', axis=1)
y = data['species']

# split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print(y_pred)

# model evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy is : {accuracy}")

# save train model
joblib.dump(model, "model/model.pkl")


