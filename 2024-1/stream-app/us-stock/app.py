import streamlit as st
import requests
import pandas as pd
import plotly.graph_objs as go

import yfinance as yf

def get_stock_data(symbol, start='2019-01-01'):
    
    #if "error" in data:
    #    st.error(f"Error: {data['error']}")
    #    return None

    stock_data = yf.download(symbol, start=start)
    return stock_data

def calculate_price_difference(stock_data):
    latest_price = stock_data.iloc[-1]["Close"]
    previous_year_price = stock_data.iloc[-252]["Close"] if len(stock_data) > 252 else stock_data.iloc[0]["Close"]
    price_difference = latest_price - previous_year_price
    percentage_difference = (price_difference / previous_year_price) * 100
    return price_difference, percentage_difference

def app():
    #-- BOLIERPLATE --#
    st.set_page_config(page_title="美股", layout="wide", page_icon="📈")
    hide_menu_style = "<style> footer {visibility: hidden;} </style>"
    st.markdown(hide_menu_style, unsafe_allow_html=True)

    st.title("📈 美股")
    popular_symbols = ["AAPL",  "NVDA", "ARM", "MSFT", "AVGO","QCOM","AMZN", "GOOGL","TSLA", "META", "BRK-B", "V", "JPM"]
    popular_symbols_c = {"AAPL":"AAPL, 蘋果", "NVDA":"Nvida, 輝達",  "ARM": "ARM, 安謀", "MSFT":"MSFT, 微軟", "AVGO":"AVGO, 高通","QCOM":"QCOM, 博通","AMZN":" AMZN, 亞馬遜", "GOOGL":"GOOGL, 谷歌","TSLA":"TSLA, 特斯拉", "META":"META, 元宇宙", "BRK-B":"BRK-B, 波客夏", "V":"V, Visa", "JPM":"JPM, 摩根"}
    symbol = st.sidebar.selectbox("Select a stock symbol, 股票 代號:", popular_symbols, index=2)

    if symbol:
        stock_data = get_stock_data(symbol)

    if stock_data is not None:
       price_difference, percentage_difference = calculate_price_difference(stock_data)
       latest_close_price = stock_data.iloc[-1]["Close"]
       max_52_week_high = stock_data["High"].tail(252).max()
       min_52_week_low = stock_data["Low"].tail(252).min()

       col1, col2, col3, col4 = st.columns(4)
       with col1:
            st.metric("Close Price, 收盤價", f"${latest_close_price:.2f}")
       with col2:
            st.metric("Price Difference (YoY), 年收益 ", f"${price_difference:.2f}", f"{percentage_difference:+.2f}%")
       with col3:
            st.metric("52-Week High, 年度最高收盤價", f"${max_52_week_high:.2f}")
       with col4:
            st.metric("52-Week Low, 年度最低收盤價", f"${min_52_week_low:.2f}")

       st.subheader(f"{popular_symbols_c[symbol]} Candlestick Chart, 交易圖")
       candlestick_chart = go.Figure(data=[go.Candlestick(x=stock_data.index, open=stock_data['Open'], 
                              high=stock_data['High'], low=stock_data['Low'], close=stock_data['Close'])])
       candlestick_chart.update_layout(title=f"{symbol} Candlestick Chart", xaxis_rangeslider_visible=False)
       st.plotly_chart(candlestick_chart, use_container_width=True)

       st.subheader("Summary, 總括")
       st.dataframe(stock_data.tail())

       st.download_button("Download Stock Data Overview, 下載資料", stock_data.to_csv(index=True), 
                          file_name=f"{symbol}_stock_data.csv", mime="text/csv")


if __name__ == "__main__":
    app()