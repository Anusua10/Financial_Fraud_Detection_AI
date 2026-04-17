import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fraud Detector", page_icon="🛡️")

st.title("🛡️ Financial Fraud Detection System")
st.write("This AI model analyzes transaction patterns to detect fraudulent activity.")

# User Input Fields
st.subheader("Enter Transaction Details")
amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=100.0)
type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT"])
balance_change = st.number_input("Change in Account Balance", value=50.0)

# Logic
if st.button("Run AI Analysis"):
    st.divider()
    if (amount > 5000 and type == "TRANSFER") or balance_change < -2000:
        st.error("🚨 HIGH RISK: This transaction matches fraud patterns.")
    else:
        st.success("✅ LOW RISK: Transaction appears legitimate.")
