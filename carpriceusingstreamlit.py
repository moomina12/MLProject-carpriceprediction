


import pandas as pd

import numpy as np
import pickle
from pickle import load
import streamlit as st

model = load(open("votreg.pkl", 'rb'))
st.title("CAR PRICE PREDICTION APP")
st.write("<h1 style='text-align: left; color: #FFD700;'>Enter the car details here </h1>", unsafe_allow_html = True)
#st.write('This app predicts the car price based on features like Present_Price	Kms_Driven	Owner	Number_of_Years_Old	Fuel_Type_Diesel	Fuel_Type_Petrol	Seller_Type_Individual	Transmission_Manual, age, bmi etc.')

#col1 = st.columns(2)

#with col1:
    #st.image('power BI.jif')

#with col2: 
#st.image('image1.jpeg')

col1, col2 = st.columns(2)


with col1:
    st.image("powerBI.gif")

with col2:
    st.image("image2.jpg")
#getting input from the user
Present_Price=st.number_input('Present_Price')
Kms_Driven=st.number_input('Kms_Driven')
#showroom_price_of_the_car = st.number_input('Present_Price')

#Car_kms_driven = st.number_input('Kms_Driven')
Owner=st.selectbox('no of owners',['0','1','2'])
#Fuel_type = st.selectbox('Fuel Type',['Petrol','Diesel' ])
Number_of_Years_Old=st.number_input('Number of years old')
#No_of_previous_owners_of_the_car = st.selectbox('no of owners',['0','1','2'])
Fuel_Type_Diesel=st.selectbox('Fuel Type',['Diesel' ])
Fuel_Type_Petrol=st.selectbox('Fuel Type',['Petrol'])
Seller_Type_Individual=st.selectbox('Seller Type'['0'])
Transmission_Manual=st.number_input('Transmission type',0)
#fuel_type = 1 if Fuel_type == 'Petrol' else 0

def predict(Present_Price,Kms_Driven,Owner,Number_of_Years_Old,Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual):
    features = np.array([Present_Price,Kms_Driven,Owner,Number_of_Years_Old,Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return prediction

if st.button('Predict'):
    prediction = predict(Present_Price,Kms_Driven,Owner,Number_of_Years_Old,Fuel_Type_Diesel, Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual)
    #prediction_text = f'<span style = "font-size:30px; color:#FFD700;">Prediction Insurance - ${prediction:.2f}</span>' 
    #st.write(prediction_text, unsafe_allow_html = True)
