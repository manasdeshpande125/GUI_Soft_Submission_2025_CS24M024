import streamlit as st
import requests
import time
import random
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

data = [
    {"Pod Name": "Avishkar-1", "Current Speed (km/h)": 100, "Battery Percentage (%)": 75, "Status": "Operational"},
    {"Pod Name": "Avishkar-2", "Current Speed (km/h)": 80, "Battery Percentage (%)": 50, "Status": "Maintenance"},
    {"Pod Name": "Avishkar-3", "Current Speed (km/h)": 120, "Battery Percentage (%)": 90, "Status": "Docked"},
    {"Pod Name": "Avishkar-4", "Current Speed (km/h)": 60, "Battery Percentage (%)": 40, "Status": "Operational"},
]

def fetch():
    url="https://tahapp.free.beeceptor.com/facts"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.write("Failed to Fun Facts")
        return None
    
hyperloop_facts=fetch()
st.title("Fun Facts About Hyperloop")

colors = ["#FFCDD2", "#F8BBD0", "#E1BEE7", "#D1C4E9", "#BBDEFB",
          "#B3E5FC", "#B2EBF2", "#B2DFDB", "#C8E6C9", "#DCEDC8"]
# box_color = colors[random]

# Iterate through the fun facts and display them
for idx, fact in enumerate(hyperloop_facts["fun_facts"], start=1):
    # st.write(f"**Fact {idx}:** {fact['fact']}")
    # st.info(f"**Fact {idx}:** {fact['fact']}")
    # time.sleep(5)
    st.markdown(
    f"""
    <div style="background-color: {random.choice(colors)}; padding: 20px; border-radius: 10px; margin: 10px 0;">
        <h4 style="color: #333;">Fact {idx}</h4>
        <p style="color: #333;">{fact['fact']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)
    time.sleep(2)
    