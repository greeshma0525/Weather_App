import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "f66cd8ae4ae8802863709c4f27de7325"   # Your API Key

def get_weather():
    city = city_entry.get()

    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 401:
            messagebox.showerror("Error", "Invalid API Key! Please check your OpenWeather account.")
            return

        if data.get("cod") != 200:
            messagebox.showerror("Error", data.get("message", "City not found"))
            return

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]

        result = f"Temperature: {temp}°C\nWeather: {desc}\nHumidity: {humidity}%"
        messagebox.showinfo("Weather Info", result)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# Tkinter UI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.config(bg="#c8eaf5")

title = tk.Label(root, text="Weather App", font=("Arial", 20, "bold"), bg="#c8eaf5")
title.pack(pady=20)

city_entry = tk.Entry(root, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

btn = tk.Button(root, text="Check Weather", font=("Arial", 12), command=get_weather)
btn.pack(pady=15)

root.mainloop()
