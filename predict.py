#This code has been coded by Lewis M.K.
import streamlit as st
import pickle
import numpy as np


# Load the model and use it to predict
model = pickle.load(open("random_forest_model_customer_churn_1.pkl", "rb"))


# Title for the page
def show_predict_page():
    st.title("Customer Churn Predictor")
    st.write("""### Please enter the below information to predict the Customer Churn. """)



#Section 1
    with st.container():
        num_col, cat_col = st.columns((1, 1))
        with num_col:
            Credit_score = st.text_input("Credit Score: *" )
        with cat_col:
            Active_Member = st.selectbox('Is the Customer Active Member?* (Yes/No)', ["","Yes", "No"])
            if Active_Member == "Yes":
                Active_Member = 1
            else:
                Active_Member = 0


#Section 2
    with st.container():
        num_col, cat_col = st.columns((1, 1))
        with num_col:
            Customer_Age = st.text_input("Age: *" )
        with cat_col:
            Credit_Card = st.selectbox('Does the Customer have Credit Card?* (Yes/No)', ["","Yes", "No"])
            if Credit_Card == "Yes":
                Credit_Card = 1
            else:
                Credit_Card = 0


#Section 3
    with st.container():
        num_col, cat_col = st.columns((1, 1))
        with num_col:
            Customer_Tenure = st.text_input("Tenure: *" )
        with cat_col:
            Select_Location = st.selectbox('Customer Location: *', ["","France", "Spain","Germany"])
            if Select_Location == "France":
                France = 1
                Spain = 0
                Germany = 0
            elif Select_Location == "Spain":
                France = 0
                Spain = 1
                Germany = 0
            elif Select_Location == "Germany":
                France = 0
                Spain = 0
                Germany = 1
            else:
                France = 0
                Spain = 0
                Germany = 0

#Section 4
    with st.container():
        num_col, cat_col = st.columns((1, 1))
        with num_col:
            Account_Balance = st.text_input("Enter the Account Balance: *" )
        with cat_col:
            Customer_Gender = st.selectbox('Gender of Customer: * (Male/Female)', ["","Male", "Female"])
            if Customer_Gender == "Male":
                Male = 1
                Female = 0
            elif Customer_Gender == "Female":
                Male = 0
                Female = 1
            else:
                Male = 1
                Female = 1

#Section 5
    with st.container():
        num_col, cat_col = st.columns((1, 1))
        with num_col:
            Product_Numbers = st.text_input("Number of Products: *" )
        with cat_col:
            Estimated_Salary = st.text_input("Enter the Estimated Salary: *" )


    ok = st.button("Predict Churn")
    st.write("""##### Please click above to predict whether the Customer will return or not. """)



# Button Click action
    if ok:
        y = np.array([[Credit_score,Active_Member,Customer_Age,Credit_Card,Customer_Tenure,France,Germany,Spain,Account_Balance,Male,Female,Product_Numbers,Estimated_Salary]])
        prediction = model.predict(y)
        if prediction == 1:
            st.success(r'''The Customer will remain.''')
        else:
            st.warning(r'''The Customer will leave.''')

