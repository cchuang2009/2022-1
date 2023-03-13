# numerical and statistical utilities
import numpy as np

# visualization requirements
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as ex

# data utitilies
import yfinance as yf
import pandas as pd
import pandas_ta
import datetime as dt

import streamlit as st

# Observe recent changes
start = dt.datetime(2019, 1, 1).strftime('%Y-%m-%d')
end =  dt.date.today()

# set ticker's symbol in yahoo stock
#ticker='2330.TW'

def get_data(ticker: str):
    
    try:
        df = yf.download(ticker, start = start, end = end)
        df['stoch_k'] = pandas_ta.stochrsi(close=df['Adj Close'],length=20).iloc[:,0]
        df['stoch_d'] = pandas_ta.stochrsi(close=df['Adj Close'],length=20).iloc[:,1]
        df['bb_lower'] = pandas_ta.bbands(close=df['Adj Close'],length=20).iloc[:,0]
        df['bb_upper'] = pandas_ta.bbands(close=df['Adj Close'],length=20).iloc[:,2]
        df['forward_1d'] = df['Adj Close'].pct_change(1).shift(-1)
        
    except Exception as e:
        st.write(e)
    
    return (
        df
    )
def get_candlestick_chart_1(df, plot_days):
    df = df[-int(plot_days):]
    
    fig = go.Figure()
    
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Adj Close'],
            name=ticker,
            showlegend=True,
        )
    )
    fig.add_trace(
        go.Line(
            x=df.index,
            y=df['bb_lower'],name='bb_lower',
        )    
    )
    fig.add_trace(
        go.Line(
            x=df.index,
            y=df['bb_upper'], name='bb_upper',
        )    
    )
    

    fig.update_xaxes(
        rangebreaks = [{'bounds': ['sat', 'mon']}],
        rangeslider_visible = False,
    )
    title=ticker+' Adj Close with Bollinger Bands'
    fig.update_layout(
        title_text=title, title_x=0.5,
        legend = {'x': 0, 'y': -0.05, 'orientation': 'h'},
        margin = {'l': 50, 'r': 50, 'b': 50, 't': 25},
        width = 800,
        height = 400,
        
    )
    
    return fig

def get_bband(df, plot_days):
    df = df[-int(plot_days):]
    title=ticker+' Adj Close with Bollinger Bands'
    fig=ex.line(df, x=df.index, y=['Adj Close','bb_lower','bb_upper'], title=title)

    fig.update_layout(title_text=title, title_x=0.5,width = 800,
        height = 400,)
    return fig

# Sidebar controls -----------------------------------------------------------
ticker = st.sidebar.text_input(
    label='Stock ticker',
    value='2330.TW',    
)

plot_days = st.sidebar.number_input(
    label='Chart viewing length',
    value=120,
    min_value=1,
    step=1,
)

st.sidebar.button(
    label='Update data',
    on_click=get_data,
    kwargs={'ticker': ticker},
)

df = get_data(ticker)
st.subheader('Price Chart')    

st.plotly_chart(
    get_bband(df,plot_days)
)

