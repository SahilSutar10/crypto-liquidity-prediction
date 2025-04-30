# 🧠 Cryptocurrency Liquidity Prediction

This project uses machine learning to predict the liquidity ratio of cryptocurrencies based on market data. The final model is deployed using Streamlit for live interaction.

## 🔧 Features
- Real-time market data ingestion (simulated via CSV)
- Feature engineering: volatility, moving averages
- ML models: Linear Regression, Random Forest, XGBoost
- Deployment using Streamlit web app

## 📁 Project Structure
```
CryptoLiquidityApp/
├── app.py
├── final_rf_model.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── crypto_combined.csv
│
├── models/
│   └── final_rf_model.pkl
│
├── eda/
│   └── EDA_Liquidity_Crypto.ipynb
│
├── docs/
│   ├── Final_Report.pdf
│   ├── HLD_LLD.md
│   └── architecture_diagram.png
```

## ▶️ How to Run
```
pip install -r requirements.txt
streamlit run app.py
```