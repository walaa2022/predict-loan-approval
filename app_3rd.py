import streamlit as st
import pandas as pd
import joblib
import numpy as np
import category_encoders
import xgboost as xgb


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def prediction(Gender, Married, Dependents, Education, Self_Employed, Credit_History, Property_Area, LoanAmount_log, Total_Income, EMI, Total_Income_log, Balance_Income):
    Total_Income = ApplicantIncome + CoapplicantIncome
    EMI = LoanAmount / Loan_Amount_Term
    Balance_Income = Total_Income - (EMI * 1000)
    Total_Income_log = np.log (Total_Income)
    LoanAmount_log = np.log (LoanAmount)
    
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    test_df.at[0,"LoanAmount_log"] = LoanAmount_log
    test_df.at[0,"Total_Income"] = Total_Income
    test_df.at[0,"EMI"] = EMI
    test_df.at[0,"Total_Income_log"] = Total_Income_log
    test_df.at[0,"Balance_Income"] = Balance_Income
    st.dataframe(test_df)
    result = model.predict(test_df)[0]
    return result

    
def main():
    st.title("Predict loan approval")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    Married = st.selectbox("Married" , ['Yes', 'No'])
    Dependents = st.selectbox("Dependents" , ['1', '2','3'])
    Education = st.selectbox("Education" , ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed" , ['Yes', 'No'])
    Credit_History = st.selectbox("Credit_History" , ['0', '1'])
    Property_Area = st.selectbox("Property_Area", ['Urban', 'Rural', 'Semiurban'])
    Total_Income = st.slider("Total_Income", min_value = 1000, max_value = 100000, value= 0, step=1 )
    LoanAmount = st.slider("LoanAmount", min_value = 9, max_value = 700, value= 0, step=1 )
    Loan_Amount_Term = st.slider("Loan_Amount_Term", min_value = 11, max_value = 500, value= 0, step=1 )
    ApplicantIncome = st.slider("ApplicantIncome", min_value = 100, max_value = 900000, value= 0, step=1 )
    CoapplicantIncome = st.slider("CoapplicantIncome", min_value =0, max_value = 50000, value= 0, step=1 )
    

    
    if st.button("predict"):
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, Credit_History, Property_Area, LoanAmount_log, Total_Income, EMI, Total_Income_log, Balance_Income)
        label = ["Approved" , "Not-approved"]
        st.text(f"The Loan will be {label[result]}")
        
if __name__ == '__main__':
    main()    
