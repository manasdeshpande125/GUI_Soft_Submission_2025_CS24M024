import streamlit as st
import pandas as pd
from entrypoint import data
st.title("Pod Comparison Tool")

# Let users select two pods for comparison
df=pd.DataFrame(data)
st.subheader("Select two pods to compare:")
pod_options = df["Pod Name"].tolist()

pod1 = st.selectbox("Select Pod 1", pod_options, key="pod1")
pod2 = st.selectbox("Select Pod 2", pod_options, key="pod2")

# Ensure different pods are selected
if pod1 == pod2:
    st.error("Please select two different pods for comparison.")
else:
    # Extract data for the selected pods
    pod1_data = df[df["Pod Name"] == pod1].iloc[0]
    pod2_data = df[df["Pod Name"] == pod2].iloc[0]

    # Combine data into a comparison table
    comparison_data = {
        "Parameter": ["Battery Percentage (%)", "Current Speed (km/h)", "Status"],
        pod1: [pod1_data["Battery Percentage (%)"], pod1_data["Current Speed (km/h)"], pod1_data["Status"]],
        pod2: [pod2_data["Battery Percentage (%)"], pod2_data["Current Speed (km/h)"], pod2_data["Status"]],
    }
    comparison_df = pd.DataFrame(comparison_data)

    # Display comparison table
    st.subheader("Comparison Table")
    st.table(comparison_df)