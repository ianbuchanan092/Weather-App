import tkinter as tk
import requests
from datetime import datetime

from config import API_KEY
CITY_NAME = "Sydney"
UNITS = "metric"

def fetch_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": UNITS
        }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
def update_weather():
    data = fetch_weather(CITY_NAME)
    
    if data.get("cod") !=200:
        status_label.config(
            text=f"Error: {data.get('message', 'Unable to fetch weather.')}"
            )
        return
    # Parse important information from the JSON
    main = data["weather"][0]["main"]
    description = data["weather"][0]["description"].capitalize()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data ["main"]["pressure"]
    wind_speed = data["wind"] ["speed"]
    
    #Convert timestamp to human-readable time
    timestamp = data["dt"]
    update_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    
    #Update labels
    city_label.config(text=f"Weather in {CITY_NAME}")
    main_label.config(text=f"{main} ({description})")
    temp_label.config(text=f"Temperaature: {temp}°C")
    feels_label.config(text=f"Feels like: {feels_like}°C")
    humid_label.config(text=f"Humidity: {humidity}%")
    pressure_label.config(text=f"Pressure: {pressure} hPa")
    wind_label.config(text=f"Wind: {wind_speed} m/s")
    status_label.config(text=f"Last updated: {update_time}")
    
    #Refresh again in 10 minutes (600,00 ms)
    root.after(600000, update_weather)
    
root = tk.Tk()
root.title("Raspberry Pi Weather Dashboard.  Coded by Ian using Python")

#Create label widgets

city_label = tk.Label(root, font=("Helvetica", 18, "bold"))
main_label = tk.Label(root, font=("Helvetica", 14))
temp_label = tk.Label(root, font=("Helvetica", 12))
feels_label = tk.Label(root, font=("Helvetica", 12))
humid_label = tk.Label(root, font=("Helvetica", 12))
pressure_label = tk.Label(root, font=("Helvetica", 12))
wind_label = tk.Label(root, font=("Helvetica", 12))
status_label = tk.Label (root, font=("Helvetica", 10), fg="gray")

#Position them in the window

city_label.pack(pady=(10, 0))
main_label.pack(pady=(5, 5))
temp_label.pack()
feels_label.pack()
humid_label.pack()
pressure_label.pack()
wind_label.pack()
status_label.pack(pady=(10, 10))

#Initial fetch and display
update_weather()

#Run the Tkinter event loop
root.mainloop()          
