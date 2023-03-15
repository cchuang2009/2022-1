import streamlit as st
import pandas as pd

# read data, 讀取資料

df=pd.read_csv("TWSE_TW-1.csv")
df.fillna('', inplace=True)

# set up Streamlit app, 建立應用程式
st.title("TWSE Stock Search, 台灣股票代號查詢")

# add search box and dropdown, 增加搜尋選擇欄位
search_term = st.text_input("Enter search term, 輸入查詢資料:")
search_by = st.selectbox("Search by column:", options=['Symbol 公司代碼', 'Name 公司名稱'])

# search for matching rows, 搜尋並列印結果
if search_term:
    if search_by == 'Symbol 公司代碼':
        result = df[df['Symbol'].str.contains(search_term)]
    elif search_by == 'Name 公司名稱':
        result = df[df['Name'].str.contains(search_term)]
    else:
        result = pd.DataFrame()
    st.write('Search ',search_term,' by ', search_by )   
    st.write(result)
    