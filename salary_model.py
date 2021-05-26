import pandas as pd
import joblib

salary = pd.read_csv('Salary_Data.csv')
x = salary['YearsExperience'].values.reshape(-1,1)
y = salary['Salary']

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)

joblib.dump(model, 'exp.pk1' )

