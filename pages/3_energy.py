import streamlit as st
import requests

def fetch():
    url="https://tahapp.free.beeceptor.com/energy1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.write("Failed to fetch weather data. Please check your API key or location.")
        return None
st.title("Energy Efficiency Tips for Transportation")
data=fetch()
if data:
    # st.write(data)
    

# Iterate through the JSON data and display topics and tips
    for topic, tips in data.items():
        st.subheader(topic.replace("_", " ").title())
        for key, tip in tips.items():
            st.write(f"{key.replace('_', ' ').title()}: {tip}")       
