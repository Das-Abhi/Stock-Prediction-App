import streamlit as st
from datetime import date

import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.graph_objects as go

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
st.title("Stock Price Prediction")

stocks = ("AAPL","GOOG","MSFT","GME")
selected_stocks = st.selectbox("Select a stock for prediction",stocks)

n_years = st.slider("Number of years for prediction",1,4)
period = n_years*365

@st.cache
def load_data(ticker):
    data = yf.download(ticker,start=START,end=TODAY)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data ...")
data = load_data(selected_stocks)
data_load_state.text("Data loaded.")

st.subheader('Raw data')
st.write(data.tail())
