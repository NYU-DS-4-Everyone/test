
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics as mt
import seaborn as sns
from sklearn.metrics import accuracy_score

### The st.title() function sets the title of the Streamlit application to "Mid Term Template - 03 Prediction Page 🧪".
st.title(" Prediction Page 👮🏻‍♀️")



### read csv files
df = pd.read_csv('df_police_fatalities_merged.csv')





###factorize binary data within the df

###gender encoding
df['Gender'] = df['Gender'].factorize()[0]

### race encoding
df['Race'] = df['Race'].factorize()[0]

### statecode encoding
df['stateCode'] = df['stateCode'].factorize()[0]

### armed encoding
df['Armed'] = df['Armed'].factorize()[0]

### mentalilness
df['Mental_illness'] = df['Mental_illness'].factorize()[0]

### flee
df['Flee'] = df['Flee'].factorize()[0]

### Manner of death 
df['Manner_of_death'] = df['Manner_of_death'].factorize()[0]

### remove commas in population so data could be more readable
df[" popEst2014 "] = pd.to_numeric(df[" popEst2014 "].str.replace(",",""))

df=df.dropna()


### The st.sidebar.selectbox() function creates a dropdown menu in the sidebar that allows users to select the target variable to predict.
list_variables = df.columns
select_variable =  st.sidebar.selectbox('🎯 Select Variable to Predict',list_variables)

### The st.sidebar.number_input() function creates a number input widget in the sidebar that allows users to select the size of the training set.

new_df= df.drop(labels=select_variable, axis=1)  #axis=1 means we drop data by columns
list_var = new_df.columns

### The st.multiselect() function creates a multiselect dropdown menu that allows users to select the explanatory variables.
output_multi = st.multiselect("Select Explanatory Variables", list_var,default= ["Race","Gender", "Flee","stateCode"])
new_df2 = new_df[output_multi]
X =  new_df2
y = df["Mental_illness"]
train_size = st.sidebar.number_input("Train Set Size", min_value=0.00, step=0.01, max_value=1.00, value=0.70)

### The train_test_split() function splits the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = train_size)

### The LogisticRegression() function creates a logistic regression model.
lm = LogisticRegression()

### The lm.fit() function fits the linear regression model to the training data.
lm.fit(X_train,y_train)

###The lm.predict() function generates predictions for the testing data.
prediction = lm.predict(X_test)

###Calculate score
score = accuracy_score(y_test, prediction)



### The st.columns() function creates two columns to display the feature columns and target column.
col1,col2 = st.columns(2)
col1.subheader("Feature Columns top 25")
col1.write(X.head(25))
col2.subheader("Target Column top 25")
col2.write(y.head(25))

### The st.subheader() function creates a subheading for the results section.
st.subheader('🎯 Results')
###print score
st.write("🎯 Accuracy %",score * 100)
