import streamlit as st
import requests
import pandas as pd

# Set up the WeatherAPI key and base URL
API_KEY = "d1278b2faba248dda4e41916252001"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
Base="http://api.weatherapi.com/v1/alerts.json"

# Define Hyperloop route locations
routes = {
    "Route 1: City A to City B": ["City A", "City B"],
    "Route 2: City C to City D": ["City C", "City D"],
    "Route 3: City E to City F": ["City E", "City F"],
}

# Streamlit app title
st.title("Hyperloop Route Weather Tracker")

# Route selection
route = st.selectbox("Select a Hyperloop Route", list(routes.keys()))
locations = routes[route]

# Fetch weather data
def fetch_weather(location):
    url = f"{BASE_URL}?key={API_KEY}&q={location}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.write("Failed to fetch weather data. Please check your API key or location.")
        return None
combined_data=[]
# Display weather data
for i in locations:
    weather_data = fetch_weather(i)
    combined_data.append(weather_data['current'])
    if weather_data:
        st.subheader(f"Weather in {i}")
        st.write(f"**Temperature**: {weather_data['current']['temp_c']}°C")
        st.write(f"**Condition**: {weather_data['current']['condition']['text']}")
        st.write(f"**Wind Speed**: {weather_data['current']['wind_kph']} km/h")
        st.write(f"**Humidity**: {weather_data['current']['humidity']}%")


# df1=pd.DataFrame(combined_data)
# st.table(df1)


# Fetch alert data
def fetch_alerts(location):
    url = f"{Base}?key={API_KEY}&q={location}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.write("Failed to fetch alert data. Please check your API key or location.")
        return None

for i in locations:
    alert_data = fetch_alerts(i)
    st.subheader(f"Alerts in {i}")
    if alert_data['alerts']['alert']:
        
        st.write(alert_data['alerts']['alert'])
    else:
        st.write("No Alerts")


# Safe speed recommendations based on weather conditions
speed_limits = {
    "Sunny": 1000,
    "Clear": 1000,
    "Partly cloudy": 900,
    "Cloudy": 850,
    "Rain": 700,
    "Thunderstorm": 500,
    "Snow": 600,
    "Fog": 600,
    "Overcast": 800,
    "Drizzle": 750,
}

def get_safe_speed(condition):
    """Get safe speed based on weather condition."""
    return speed_limits.get(condition, 800)  # Default to 800 km/h for unknown conditions

# speed=pd.DataFrame(list(speed_limits))
# st.table(speed)
# st.subheader('Speed Limit')
# st.write(get_safe_speed(weather_data['current']['wind_kph']))




def fetch_weather_1(location):
    url = f"{BASE_URL}?key={API_KEY}&q={location}&alerts=yes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # alerts = data.get("alerts", {}).get("alert", [])
        # alert_messages = [alert["headline"] for alert in alerts] if alerts else ["No alerts"]
        condition = data["current"]["condition"]["text"]
        return {
            "Location": location,
            "Temperature (°C)": data["current"]["temp_c"],
            "Condition": condition,
            "Wind Speed (km/h)": data["current"]["wind_kph"],
            "Humidity (%)": data["current"]["humidity"],
            # "Alerts": " | ".join(alert_messages),
            "Recommended Speed (km/h)": get_safe_speed(condition),
        }
    else:
        st.error(f"Failed to fetch weather data for {location}.")
        return None

# Fetch data for both cities
weather_data = [fetch_weather_1(location) for location in locations]

# Display weather data in a table if both cities are successful
if None not in weather_data:
    df = pd.DataFrame(weather_data)
    st.subheader(f"Weather and Speed Recommendations for {route}")
    st.table(df)



