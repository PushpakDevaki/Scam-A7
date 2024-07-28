import streamlit as st
import requests

# Function to get weather data
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Streamlit App
def main():
    st.title("Weather Tracker")

    api_key = st.text_input("Enter your OpenWeatherMap API Key")
    city_name = st.text_input("Enter City Name")

    if st.button("Get Weather"):
        if api_key and city_name:
            weather_data = get_weather(city_name, api_key)
            if weather_data["cod"] != "404":
                main_weather = weather_data["weather"][0]["main"]
                description = weather_data["weather"][0]["description"]
                temp = weather_data["main"]["temp"]
                pressure = weather_data["main"]["pressure"]
                humidity = weather_data["main"]["humidity"]
                wind_speed = weather_data["wind"]["speed"]
                
                st.subheader(f"Weather in {city_name}")
                st.write(f"**Main:** {main_weather}")
                st.write(f"**Description:** {description}")
                st.write(f"**Temperature:** {temp} °C")
                st.write(f"**Pressure:** {pressure} hPa")
                st.write(f"**Humidity:** {humidity} %")
                st.write(f"**Wind Speed:** {wind_speed} m/s")
            else:
                st.error("City not found")
        else:
            st.error("Please provide both API Key and City Name")

if __name__ == "__main__":
    main()
