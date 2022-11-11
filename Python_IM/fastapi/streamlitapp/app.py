# >  streamlit run app.py
# ToDo: model order of feature ->features below

import streamlit as st
import numpy as np
import pandas as pd
import requests
import json

#import sklearn
#from pycaret.regression import load_model, predict_model

df = pd.read_csv('Laptop_price_EDA.csv')
st.title('Laptop Prices Predictor ')

#model = joblib.load('deployment_20221101.pkl')
#model = load_model('deployment_20221101_1')


st.markdown( "## 手提電腦估價")
st.subheader('Laptop Details:')


features_=['Company_name_encoded', 'TypeName_name_encoded',
           'Cpu_brand_name_encoded', 'CPU_vel', 'GPU_name_encoded', 'Ram',
           'first_type_name_encoded', 'first_size', 'second_type_name_encoded',
           'second_size', 'Touchscreen', 'Ips', 'Inches', 'ppi', 'os_name_encoded',
           'Price']

def label_dict(df_,feature,label_='_name_encoded'):
    feature_lab=feature+label_
    return {k: v for k, v in zip(df_[feature].unique(), df_[feature_lab].unique() )}

def select_type(opt,feature_opt):
    dic_=df_lab.loc[df_lab.index==feature_opt,'label'][0]
    #print(feature_opt, opt," : value ",dic_[opt])
    return dic_[opt]

cat_f=['Company', 'TypeName','Cpu_brand', 'GPU', 'first_type', 'second_type','os']

label_array=[]
for cat in cat_f:
    #cat_=cat+'_dic'
    cat_=label_dict(df,cat) 
    label_array.append(cat_)

df_lab=pd.DataFrame(index=cat_f)
df_lab['label']=label_array    
    

#label_dict(df_dep,'Company')


Company = st.selectbox("Company", options=df["Company"].unique())
Company_of_laptop = select_type(Company,'Company')

TypeName=st.selectbox("Type of Laptop", options=df["TypeName"].unique())
TypeName_of_laptop = select_type(TypeName,'TypeName')

Cpu_brand = st.selectbox("Type of the CPU", options=df["Cpu_brand"].unique())
Cpu_brand_of_laptop = select_type(Cpu_brand,'Cpu_brand')

GPU = st.selectbox("Type of the  GPU", options=df["GPU"].unique())
GPU_of_laptop = select_type(GPU,'GPU')

first_type = st.selectbox("First Storage", options=df["first_type"].unique())
first_type_of_laptop = select_type(first_type,'first_type')

second_type = st.selectbox("Second Storage", options=df["second_type"].unique())
second_type_of_laptop = select_type(second_type,'second_type')

os = st.selectbox("Operation System", options=df["os"].unique())
os_of_laptop = select_type(os,'os')

# RAM [ 8, 16,  4,  2, 12,  6, 32, 24, 64]

ram_in_gb = st.number_input('RAM in GB', step=4, min_value=4)
size_in_inches = st.number_input('Size of the laptop in Inches', step=0.1, min_value=10.0)
CPU_vel = st.number_input('Velocity of CPU', step=0.4, min_value=1.0)
touchscreen  = st.radio("Touchscreen (0-No,1-Yes)", options=[0, 1])
Ips  = st.radio("IPS Screen (0-No,1-Yes)", options=[0, 1])
#X_res = st.number_input('Revolustion of X', step=200, min_value=1200)
#Y_res = st.number_input('Revolustion of Y', step=100, min_value=800)
ppi = st.number_input('Revolustion of ppi', step=10, min_value=90)
first_size = st.number_input('Size of First Storage', step=32, min_value=32)
second_size = st.number_input('Size of Second Storage', step=32, min_value=0)
#Weight = st.number_input('Weight', step=0.2, min_value=0.6)

# 'Inches','Ram','CPU_vel','Touchscreen', 'Ips', 'X_res','Y_res', 'ppi', 'first_size','second_size', 'Weight',
# 'Company_name_encoded','TypeName_name_encoded','Cpu_brand_name_encoded', 'GPU_name_encoded', 'first_type_name_encoded',
# 'second_type_name_encoded', 'os_name_encoded'



features=[Company_of_laptop, TypeName_of_laptop, Cpu_brand_of_laptop, CPU_vel, GPU_of_laptop, ram_in_gb, \
          first_type_of_laptop, first_size, second_type_of_laptop, second_size, \
          touchscreen, Ips, size_in_inches, ppi, os_of_laptop]
final_features = np.array(features).reshape(1, -1)

if st.button('Predict'):
    prediction=requests.post(url="http://127.0.0.1:8000/predict",data=final_features)
    #prediction = model.predict(final_features)
    st.balloons()
    #st.success(f'Your predicted price of the laptop is {round(prediction[0],3)}')
    #st.success(f'Predicted Price of the Laptop is about NT$ {final_features}')
    st.success(f'Predicted Price of the Laptop is about NT$ {int(prediction[0])}')
    