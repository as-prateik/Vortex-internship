# -*- coding: utf-8 -*-
"""Linear regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PcJN9gfvCb9YZ6JCYZTwgtIKrLXpJmRH
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as lr

df0 = pd.read_csv("Mail_Customers.csv")

df0.head(6)

df0.tail(6)

df0.info()

df0 = df0.rename(columns={"Genre": "Gender"})

df0.info()

# Linear Regression

df1 = pd.get_dummies(df0["Gender"])
df1.head()

df2 = pd.concat((df1, df0), axis=1)
df2 = df2.drop(["Gender"], axis=1)
df2 = df2.drop(["Male"], axis=1)
df2 = df2.rename(columns={"Female": "Gender"})
print(df2)

x = df2[['Annual Income (k$)']]
y = df2['Spending Score (1-100)']

model = lr()
model.fit(x,y)

plt.scatter(x,y,color ='black', label = 'Data')
plt.plot(x,model.predict(x),color = 'green', label = 'regression')
plt.xlabel('Gender')
plt.ylabel('Annual income')
plt.title('Linear Regression')
plt.legend()
plt.show()

r2_score = model.score(x, y)
print(f"R-squared value: {r2_score}")



