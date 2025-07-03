# 💳 Credit Card Fraud Detection App

This project is an end-to-end Machine Learning pipeline that detects fraudulent credit card transactions using classification algorithms such as **Logistic Regression**, **Decision Tree**, and **XGBoost**.

The app is built using **Streamlit** and allows users to input transaction features and get real-time fraud predictions.

---

## 🔍 Features

- End-to-end fraud detection ML pipeline
- Handles imbalanced data using **SMOTE**
- Trained and evaluated using:
  - ROC-AUC
  - F1-Score
- Deployable **Streamlit Web App**
- Interactive prediction based on input features
- Sidebar navigation using `streamlit-option-menu`

---

## 🛠️ Tech Stack

- Python, Jupyter Notebook
- Pandas, NumPy, scikit-learn, XGBoost
- Streamlit, joblib
- Google Colab (training)
- Streamlit Cloud (deployment)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/fayazahemed/fraud-detection-streamlit.git
cd fraud-detection-streamlit
pip install -r requirements.txt
streamlit run app.py
