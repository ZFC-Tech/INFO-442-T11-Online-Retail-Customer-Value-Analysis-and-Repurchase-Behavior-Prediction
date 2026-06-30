import streamlit as st
import pandas as pd

st.set_page_config(page_title="INFO442 Project", layout="wide")

st.title("Online Retail Customer Value Analysis")

st.write(
    "This application demonstrates customer value analysis and repurchase prediction."
)

st.header("Dataset Preview")

try:
    df = pd.read_csv("cleaned_online_retail.csv")
    st.write(df.head())
except Exception as e:
    st.error(f"Unable to load dataset: {e}")

st.header("Dataset Information")

if "df" in locals():
    st.write(df.describe())

st.header("Project Summary")

st.markdown("""
### Objectives
- Customer segmentation
- RFM analysis
- Repurchase prediction

### Business Value
Identify high-value customers and support marketing decisions.
""")
