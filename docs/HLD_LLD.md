# 📘 High-Level Design (HLD)

## Project Overview
This project predicts the liquidity of cryptocurrencies using ML. Liquidity is computed as volume / market cap. The model is deployed using Streamlit.

## Modules
- Data Loading
- Preprocessing
- Feature Engineering
- Model Training
- Deployment

# 🧾 Low-Level Design (LLD)

### Data Pipeline
1. Load CSVs
2. Merge & fill missing data
3. Feature engineering

### Model Pipeline
1. Train-test split
2. Train Random Forest
3. Save model as .pkl

### Deployment
- Streamlit app.py loads the model
- Takes user input and predicts liquidity