import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = '52bba48ef4ecb54e43b2555da1df07d0'  # Your provided API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()

    if data.get('cod') != 200:
        weather_result.set(f"Error: {data.get('message', 'Cannot fetch weather data')}")
        result_label.config(fg='red')
        return

    weather_desc = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    result = (f"Weather in {city.title()}:\n"
              f"Description: {weather_desc}\n"
              f"Temperature: {temp}°C\n"
              f"Humidity: {humidity}%\n"
              f"Wind Speed: {wind_speed} m/s")
    weather_result.set(result)
    result_label.config(fg='white')

root = tk.Tk()
root.title("🌤️ Weather App")
root.geometry("450x350")
root.configure(bg="#264653")  # Dark blue-green background

# Configure grid for responsiveness
root.columnconfigure(0, weight=1)
root.rowconfigure([0, 1, 2, 3], weight=1)

# Label for input
label = tk.Label(root, text="Enter city name:", font=("Helvetica", 14), bg="#264653", fg="#f4a261")
label.grid(row=0, column=0, sticky='w', padx=15, pady=(15,5))

# Entry box
city_entry = tk.Entry(root, font=("Helvetica", 12), bd=3, relief='ridge')
city_entry.grid(row=1, column=0, sticky='ew', padx=15)

# Button
get_weather_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12, 'bold'), bg="#2a9d8f", fg="white",
                               activebackground="#e76f51", activeforeground="white", command=get_weather)
get_weather_button.grid(row=2, column=0, sticky='ew', padx=15, pady=15)

# Result label
weather_result = tk.StringVar()
result_label = tk.Label(root, textvariable=weather_result, font=("Helvetica", 13), bg="#264653", fg="white", justify='left', anchor='nw')
result_label.grid(row=3, column=0, sticky='nsew', padx=15, pady=(0,15))

root.mainloop()
