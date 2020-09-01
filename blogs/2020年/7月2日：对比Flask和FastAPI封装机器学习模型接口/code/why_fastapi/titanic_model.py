# Import dependencies
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# Load the dataset in a dataframe
url = r"D:\git_project\mpi\data\titanic\train.csv"
df = pd.read_csv(url)
# Only four features
include = ['Age', 'Sex', 'Embarked', 'Survived']
df_ = df[include]
# Data Preprocessing
categoricals = []
for col, col_type in df_.dtypes.iteritems():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df_[col].fillna(0, inplace=True)
df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

# Logistic Regression classifier
x = df_ohe[df_ohe.columns.difference(['Survived'])]
y = df_ohe['Survived']
lr = LogisticRegression(solver="liblinear")
lr.fit(x, y)

# Save your model
joblib.dump(lr, 'model.pkl')
print("Model dumped!")
# Load the model that you just saved
lr = joblib.load('model.pkl')
# Saving the data columns from training
model_columns = list(x.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")