#!/usr/bin/env python
# coding: utf-8

# In[1]:

#import library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.ticker as mtick
import streamlit as st
import joblib
import xgboost

#Dataframe


def main():
    st.title("Aplikasi Simpan Data")
    # Membuat daftar untuk menyimpan data inputan
    data_list = []

    # Definisikan list pilihan untuk beberapa parameter
    contract_options = ['Month-to-month', 'One year', 'Two year']
    internet_options = ['DSL', 'Fiber optic', 'No']
    payment_options = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']

    # Menampilkan input form
    # Input untuk gender
    gender = st.selectbox('Gender', ['Male', 'Female'])
    if gender == "Male":
        gender = 0
    else:
        gender = 1
    # input untuk senior citizen
    senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
    if senior_citizen == "Yes":
        senior_citizen = 1
    else:
        senior_citizen = 0
    # input untuk partner
    partner = st.selectbox('Partner', ['No', 'Yes'])
    if partner == "Yes":
        partner = 1
    else:
        partner = 0
    # input untuk dependents
    dependents = st.selectbox('Dependents', ['No', 'Yes'])
    if dependents == "Yes":
        dependents = 1
    else:
        dependents = 0
    # slider untuk tenure
    tenure = st.slider('Tenure (months)', min_value=1, max_value=72, value=12)
    # input untuk phone service
    phone_service = st.selectbox('Phone Service', ['No', 'Yes'])
    if phone_service == "Yes":
        phone_service = 1
    else:
        phone_service = 0
    # input untuk multiple lines
    multiple_lines = st.selectbox('Multiple Lines', ['No phone service', 'No', 'Yes'])
    if multiple_lines == "Yes":
        multiple_lines = 1
    elif multiple_lines == "No":
        multiple_lines = 0
    else:
        multiple_lines = 2
    # input untuk internet service
    internet_service = st.selectbox('Internet Service', internet_options)
    if internet_service == "DSL":
        internet_service = 1
    elif internet_service == "No":
        internet_service = 0
    else:
        internet_service = 2
    # Input untuk online security
    online_security = st.selectbox('Online Security', ['No internet service', 'No', 'Yes'])
    if online_security == "Yes":
        online_security = 1
    elif online_security == "No":
        online_security = 0
    else:
        online_security = 2
    # 
    online_backup = st.selectbox('Online Backup', ['No internet service', 'No', 'Yes'])
    if online_backup == "Yes":
        online_backup = 1
    elif online_backup == "No":
        online_backup = 0
    else:
        online_backup = 2
    # 
    device_protection = st.selectbox('Device Protection', ['No internet service', 'No', 'Yes'])
    if device_protection == "Yes":
        device_protection = 1
    elif device_protection == "No":
        device_protection = 0
    else:
        device_protection = 2
    # 
    tech_support = st.selectbox('Tech Support', ['No internet service', 'No', 'Yes'])
    if tech_support == "Yes":
        tech_support = 1
    elif tech_support == "No":
        tech_support = 0
    else:
        tech_support = 2
    # 
    streaming_tv = st.selectbox('Streaming TV', ['No internet service', 'No', 'Yes'])
    if streaming_tv == "Yes":
        streaming_tv = 1
    elif streaming_tv == "No":
        streaming_tv = 0
    else:
        streaming_tv = 2
    # 
    streaming_movies = st.selectbox('Streaming Movies', ['No internet service', 'No', 'Yes'])
    if streaming_movies == "Yes":
        streaming_movies = 1
    elif streaming_movies == "No":
        streaming_movies = 0
    else:
        streaming_movies = 2
    # 
    contract = st.selectbox('Contract', contract_options)
    if contract == "One year":
        contract = 1
    elif contract == "Month-to-month":
        contract = 0
    else:
        contract = 2
    # 
    paperless_billing = st.selectbox('Paperless Billing', ['No', 'Yes'])
    if paperless_billing == "Yes":
        paperless_billing = 1
    else:
        paperless_billing = 0
    # 
    payment_method = st.selectbox('Payment Method', payment_options)
    if payment_method == "Mailed check":
        payment_method = 1
    elif payment_method == "Electronic check":
        payment_method = 0
    elif payment_method == "Bank transfer (automatic)":
        payment_method = 2 
    else:
        payment_method = 3
    # 
    monthly_charges = st.number_input('Monthly Charges', value=50.0)
    # 
    total_charges = st.number_input('Total Charges', value=100.0)
    # ---------------

    # Menampilkan tombol Submit
    if st.button("Submit"):
        # Menyimpan data inputan ke dalam daftar
        data_list.append({
            'gender': gender,
            'SeniorCitizen': senior_citizen,
            'Partner': partner,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phone_service,
            'MultipleLines': multiple_lines,
            'InternetService': internet_service,
            'OnlineSecurity': online_security,
            'OnlineBackup': online_backup,
            'DeviceProtection': device_protection,
            'TechSupport': tech_support,
            'StreamingTV': streaming_tv,
            'StreamingMovies': streaming_movies,
            'Contract': contract,
            'PaperlessBilling': paperless_billing,
            'PaymentMethod': payment_method,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges
        })
        st.success("Data berhasil disimpan!")
    
    st.write(data_list)

    df = pd.DataFrame(data_list)
    st.write(df)

    # Mencari value dari Churn
    loaded_model = joblib.load('churn_xgbrf_model_2.pkl')
    preds = loaded_model.predict(df)
    st.write("Hasilnya sama dengan : ")
    st.write(preds)

if __name__ == "__main__":
    main()


