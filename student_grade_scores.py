# -*- coding: utf-8 -*-
"""Student_grade_scores

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13e-4b_jtw_vMjTdKB4wiPKLXWrclTvOy

# **Importing the libraries**
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score

"""# **Importing the Dataset**

First let us remove the unwanted columns or, in other words which does not have a considerable effect on the desired results for both training and predictions.

Making a list of all the column titles to remove which will be used later. This list was previously analysed and concluded as not important.
"""

to_remove = ['school', 'sex', 'age', 'Mjob', 'Fjob', 'reason',
             'guardian', 'paid', 'activities', 'nursery', 'higher',
             'internet', 'romantic', 'freetime', 'goout', 'Dalc', 'Walc']

"""Using Pandas we import the dataset in CSV foramt, but the the delimiter is not a comma (,) but a semicolon (;)."""

data = pd.read_csv('student-mat.csv', delimiter=';')

print(data.head())
data = data.drop(to_remove, axis=1)

print(data.head())

"""# **Analysing the data using barplots**"""

sns.set(style='ticks', context='talk')
sns.set(font_scale=2)

"""Plotting the relationship between each feature considered with the dependent variable (G3) and analysing the impact of different classes in that feature.

The student's address (Urban and Rural)
"""

sns.barplot(x='address', y='G3', data=data)

"""There is no much difference between Rural and Urban students even rural has less scores, when we consider a huge data it does not really matter.

---

Family size and parents status
"""

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.subplot(1, 2, 1)
sns.barplot(x='famsize', y='G3', data=data)
plt.xlabel('Family size', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.subplot(1, 2, 2)
sns.barplot(x='Pstatus', y='G3', data=data)
plt.xlabel('Parents status', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.tight_layout()

plt.show()

"""---

Mother's education and Father's education
"""

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.subplot(1, 2, 1)
sns.barplot(x='Medu', y='G3', data=data)
plt.xlabel("Mother's education", fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.subplot(1, 2, 2)
sns.barplot(x='Fedu', y='G3', data=data)
plt.xlabel("Father's education", fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.tight_layout()

plt.show()

"""The first thing we see from the above plot is that we have larger score for 0, the reason is that the data does not contain much of 0 education values and if either Father or mother has value 0 the other parent will have a greater value.

---

### **Some obvious features that can be considered from the dataset.**

Travel time and study time
"""

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.subplot(1, 2, 1)
sns.barplot(x='traveltime', y='G3', data=data)
plt.xlabel('travel time', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
plt.subplot(1, 2, 2)
sns.barplot(x='studytime', y='G3', data=data)
plt.xlabel('Study time', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.show()

"""---

Total number of failures of a student
"""

sns.barplot(x='failures', y='G3', data=data)
plt.xlabel('Failures', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.show()

"""The above two plots shows that less travela time and more study time gives better results and less failures gives better results.

---

The coming up plots are the features which does not depend much on the student

School support and family support
"""

plt.subplot(1, 2, 1)
sns.barplot(x='schoolsup', y='G3', data=data)
plt.xlabel('School support', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.subplot(1, 2, 2)
sns.barplot(x='famsup', y='G3', data=data)
plt.xlabel('Family support', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.show()

"""---

Family relationship and health of an individual student
"""

plt.subplot(1, 2, 1)
sns.barplot(x='famrel', y='G3', data=data)
plt.xlabel('Family relationship', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')

plt.subplot(1, 2, 2)
sns.barplot(x='health', y='G3', data=data)
plt.xlabel('Health', fontsize=15, fontweight='bold')
plt.ylabel('G3', fontsize=15, fontweight='bold')


plt.tight_layout()
plt.show()

"""From the data it seems like family relationship and health really did not matter for these students for their scores.

Absences
"""

sns.barplot(x='G3', y='absences', data=data)
plt.xlabel('G3', fontsize=25, fontweight='bold')
plt.ylabel('Absences', fontsize=25, fontweight='bold')

plt.tight_layout()
plt.show()

"""From the above plot we can clearly see that less absences leads to a better scoring

Lets us consider G1 and G2, because these two values are the results of all the above considered features and G can also be predicited by training with just G1 and G2.
"""

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
sns.barplot(x='G1', y='G3', data=data)
plt.xlabel('G1', fontsize=20, fontweight='bold')
plt.ylabel('G3', fontsize=20, fontweight='bold')

plt.show()

plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)
sns.barplot(x='G2', y='G3', data=data)
plt.xlabel('G2', fontsize=20, fontweight='bold')
plt.ylabel('G3', fontsize=20, fontweight='bold')

plt.show()

"""We can clearly identify that the greater the scores of G1 and G2 the greater is G3.

---

## **Using Regression for training prediction**

First we have to separate the data into independent variables (x) and dependent variables (y)

The *intersection* drops G3 column except all the columns whereas the *difference* drops all the columns except G3.
"""

x = data.iloc[:, :-1].values     
y = data.iloc[:, -1].values

"""There are some string values that needs to be encoded, the columns that contains strings are binary values."""

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0, 1, 2, 8, 9])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

"""### **Splitting the dataset into test and train set**"""

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

"""## **Training the regression models on the training set**

linear regression - for each model the training data consists of 80% and test data consists of 20% from the dataset.

The regression model is trained by fitting it with x_train and y_train
"""

regressor = LinearRegression()
regressor.fit(x_train, y_train)

"""Predcting the test results from the test set and verifying it with the original test set results."""

y_pred = regressor.predict(x_test)

for i in range(len(y_pred)):
    print("Y_pred: {}, x_test: {}, y_test: {}".format(y_pred[i], x_test[i], y_test[i]))

"""The constants and intercepts of formula of regression and the r2 score"""

print("constants: \n", regressor.coef_)         # The slope
print("intercepts: \n", regressor.intercept_)   # The intercept points

print(r2_score(y_pred, y_test))

"""K-fold cross validation for accuracy and standard deviation of the model, k_fold cross validation uses different set of test data for the validation, the number of test folds is equal to the *cv* parameter."""

accuracies = cross_val_score(estimator=regressor, X=x_train, y=y_train, cv=10)

print('Linear regression')

print("Accuracy with k_fold cross validation: {:.2f} %".format(accuracies.mean() * 100))
print("Standard deviation with k_fold cross validation: {:.2f} %".format((accuracies.std() * 100)))

"""---

Polynomial regression
"""

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=5)
x_poly = poly_reg.fit_transform(x_train)

regressor = LinearRegression()
regressor.fit(x_poly, y_train)

y_pred = regressor.predict(poly_reg.transform(x_test))

accuracies = cross_val_score(estimator=regressor, X=x_train, y=y_train, cv=10)

print('Polynomial regression')

print("Accuracy with k_fold cross validation: {:.2f} %".format(accuracies.mean() * 100))
print("Standard deviation with k_fold cross validation: {:.2f} %".format((accuracies.std() * 100)))

"""---

Decision tree model has a very poor results in this case
"""

# training the decision tree model

from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x_train, y_train)


# Predicting the new results

y_pred = regressor.predict(x_test)

accuracies = cross_val_score(estimator=regressor, X=x_train, y=y_train, cv=10)

print('Decision tree')

print("Accuracy with k_fold cross validation: {:.2f} %".format(accuracies.mean() * 100))
print("Standard deviation with k_fold cross validation: {:.2f} %".format((accuracies.std() * 100)))

"""---

Random forest regrssion model
"""

# training the decision tree model

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(x_train, np.ravel(y_train))


# Predicting the new results

y_pred = regressor.predict(x_test)

accuracies = cross_val_score(estimator=regressor, X=x_train, y=y_train, cv=10)

print('Decision tree')

print("Accuracy with k_fold cross validation: {:.2f} %".format(accuracies.mean() * 100))
print("Standard deviation with k_fold cross validation: {:.2f} %".format((accuracies.std() * 100)))

"""---

XG boost with the best score so far with k-fold cross validation
"""

# training the XG boost model

from xgboost import XGBRegressor
regressor = XGBRegressor()
regressor.fit(x_train, y_train)


# Predicting the new results

y_pred = regressor.predict(x_test)


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator=regressor, X=x_train, y=y_train, cv=10)

print('XG boost')

print("Accuracy with k_fold cross validation: {:.2f} %".format(accuracies.mean() * 100))
print("Standard deviation with k_fold cross validation: {:.2f} %".format((accuracies.std() * 100)))

"""To improve the model accuracies, we can try to delete some more columns or to include them.

---

---
"""