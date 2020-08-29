import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title('Stock Market Forecasting of Nabil Bank')

st.text('The graph below is the time series forecasting of the stock prices of Nabil Bank upto next 20 weeks')

forecast_data=pd.read_csv("Data/predicted_forecasts.csv",
                 usecols=['forecast','Date'],
                 )

prev_data = pd.read_csv("Data/data1.csv",
                usecols=['Date', 'open', 'high', 'low', 'close', 'vol'],
                )

# if st.checkbox('Show dataframe of Nabil Bank'):
#     st.dataframe(prev_data)
#     chartdata_open = prev_data['open']
#     chartdata_high = prev_data['high']
#     chartdata_low = prev_data['low']
#     chartdata_close = prev_data['close']
#     chartdata_vol = prev_data['vol']


# column = st.selectbox(
#     'What column do you want to display?',
#      prev_data.columns)
    
# prev_data = prev_data.rename(columns = {'Date':'index'}).set_index('index')
# prev_data[column]
# st.line_chart(prev_data[column])

forecast_data= forecast_data.rename(columns = {'Date':'index'}).set_index('index')
forecast_data = forecast_data.rename(columns = {'forecast':'close'})
forecast_data
st.line_chart(forecast_data)





