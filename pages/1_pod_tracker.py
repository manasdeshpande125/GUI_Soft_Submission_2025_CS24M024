import streamlit as st
import pandas as pd
from TAH_GUI import data

st.title("Pod Tracker")



df = pd.DataFrame(data)

status_filter = st.selectbox(
    "Filter by Status", options=["All"] + list(df["Status"].unique())
)

if status_filter == "All":
    filtered_df = df
else:
    filtered_df = df[df["Status"] == status_filter]

sort_option = st.selectbox(
    "Sort by", options=["Pod Name", "Current Speed (km/h)", "Battery Percentage (%)"]
)
sorted_df = filtered_df.sort_values(by=sort_option, ascending=True)

# Display the DataFrame
st.dataframe(sorted_df)