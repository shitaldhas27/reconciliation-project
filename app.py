import streamlit as st
import pandas as pd

st.title("Reconciliation Dashboard")

df = pd.read_csv("final_output.csv")

st.dataframe(df)

st.bar_chart(df["status"].value_counts())

st.metric("Total", len(df))
st.metric("Errors", len(df[df["status"] != "Matched"]))

csv = df.to_csv(index=False)

st.download_button("Download Report", csv, "report.csv", "text/csv")