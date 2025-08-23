Weather App

A simple Python weather application with a graphical user interface (GUI) built using Tkinter. It fetches live weather data from OpenWeatherMap API, displaying temperature, humidity, wind speed, and weather description for any city entered.

---

Features

- Responsive GUI built with Tkinter
- Fetches live weather data using OpenWeatherMap API
- Displays weather description, temperature (°C), humidity, and wind speed
- Shows error messages for invalid city names or API issues
- Stylish colors and fonts for improved user experience

---

How to Use

1. Clone the repository:
   git clone <repository-url>
   cd <repository-folder>

2. (Optional) Create and activate a Python virtual environment:
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Get your own OpenWeatherMap API key by signing up at https://openweathermap.org/.

5. Open the Python script file (e.g., weather_app.py) in a text editor.

6. Find the line starting with:
   api_key = 'your_api_key_here'
   Replace the placeholder with your actual API key. For example:
   api_key = '52bba48ef4ecb54e43b2555da1df07d0'

7. Save the file.

8. Run the app:
   python weather_app.py

9. Enter any city name in the window and click "Get Weather" to see current weather information.

---

How It Works

- Uses the requests library to fetch weather data from the OpenWeatherMap API via HTTP GET requests.
- Parses the JSON response to extract key weather information (description, temperature, humidity, wind speed).
- Displays this data inside a styled Tkinter GUI window.
- Handles API errors and invalid user input with friendly messages.

---

Customization

- Change GUI colors, fonts, and window size in the script to suit your preferences.
- Extend the app by adding more weather metrics, forecast data, or visual graphics.
- To use a different weather API, update the `base_url` and modify parsing logic for the new API's data structure.

---

Dependencies

- Python 3.x
- requests (install with `pip install -r requirements.txt`)
- Tkinter (comes bundled with Python standard library)

---

Feel free to contribute, open issues, or request new features!

