import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# Load the dataset
data=pd.read_csv("spam.csv")

# remove duplicates
data.drop_duplicates(inplace=True)

# check for null values
data.isnull().sum()


data['Category'] = data['Category'].replace(['ham','spam'],['Not Spam','Spam'])

# Split the dataset into features and target variable
X = data['Message']
y = data['Category']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Convert text data into numerical features using CountVectorizer
cv=CountVectorizer(stop_words='english')
X_train=cv.fit_transform(X_train)

# Creating the model
model=MultinomialNB()

# Train the model
model.fit(X_train,y_train)

# Test the model
X_test=cv.transform(X_test)
# print(model.score(X_test,y_test))

# Predict the data

def predict(message):
     input_message=cv.transform([message]).toarray()
     result=model.predict(input_message)
     return result

st.header("Spam Detection ")

input_mess=st.text_input("Enter a message to check if it's spam or not", key="input_message")

if st.button("Validate"):
    output=predict(input_mess)
    st.markdown(output[0])
    
