import streamlit as st
import pickle
import numpy as np

# Load the trained Random Forest model
with open('final_rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title('🚀 Cryptocurrency Liquidity Prediction')

st.markdown("""
Fill in the market details below to predict the **Liquidity Ratio** of a cryptocurrency.
""")

# Input fields
price = st.number_input('Current Price (USD)', min_value=0.0, format="%.4f")
change_1h = st.number_input('Price Change 1h (%)', format="%.4f")
change_24h = st.number_input('Price Change 24h (%)', format="%.4f")
change_7d = st.number_input('Price Change 7d (%)', format="%.4f")
volume_24h = st.number_input('24h Volume (USD)', min_value=0.0, format="%.4f")
market_cap = st.number_input('Market Cap (USD)', min_value=0.0, format="%.4f")
price_ma_5 = st.number_input('5-Day Moving Avg', min_value=0.0, format="%.4f")
price_volatility_5 = st.number_input('5-Day Volatility', min_value=0.0, format="%.4f")
price_change_rate = st.number_input('Abs 24h Price Change (%)', format="%.4f")

if st.button('Predict Liquidity'):
    input_data = np.array([[price, change_1h, change_24h, change_7d, volume_24h, market_cap, price_ma_5, price_volatility_5, price_change_rate]])
    prediction = model.predict(input_data)
    st.success(f'🔮 Predicted Liquidity Ratio: {prediction[0]:.6f}')
