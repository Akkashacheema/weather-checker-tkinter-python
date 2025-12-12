# Weather Checker – Python Tkinter Application

A Python-based desktop application that retrieves and displays **real-time weather information** using the **OpenWeatherMap API**. The application features a clean graphical interface built with **Tkinter** and allows users to check current weather conditions for cities through a simple and interactive UI.

---

## 📌 Project Description

The **Weather Checker** is a desktop GUI application developed using **Python and Tkinter** to fetch and display live weather data such as temperature, humidity, wind speed, and weather description. Users enter a city name, and the application retrieves real-time data from the OpenWeatherMap API and presents it in a user-friendly format.

The project demonstrates practical integration of APIs with frontend GUI development, including error handling, background processing, and data persistence through report saving.

---

## 🎯 Objectives

- Understand how REST APIs work in Python
- Fetch real-time weather data using OpenWeatherMap API
- Design a graphical user interface with Tkinter
- Integrate backend API calls with frontend GUI
- Improve skills in Python GUI and API-based development

---

## ✨ Features

- Real-time weather data retrieval
- Tkinter-based desktop GUI
- Displays temperature, humidity, wind speed, and description
- Supports saving weather reports as text files
- Error handling for invalid city names
- Simple and intuitive user interface

---

## 🛠️ Tools & Technologies

| Tool | Description |
|----|----|
| Python | Core programming language |
| Tkinter | GUI framework |
| Requests | HTTP requests to API |
| OpenWeatherMap API | Live weather data source |

---

## 📁 Project Structure

```text
weather-checker-tkinter-python/
│
├─ src/
│  └─ weather_gui.py
│
├─ assets/
│  └─ screenshot.png
│
├─ docs/
│  └─ Weather_Checker_Project_Report.docx
│
├─ requirements.txt
├─ .gitignore
├─ LICENSE
└─ README.md
⚙️ Installation & Setup
Step 1: Clone the Repository
git clone https://github.com/<your-username>/weather-checker-tkinter-python.git
cd weather-checker-tkinter-python

Step 2: Create Virtual Environment (Recommended)
python -m venv .venv

<img width="900" height="635" alt="image" src="https://github.com/user-attachments/assets/c184cfba-b742-4f6b-9800-66724ade35a3" />

Activate it:

Windows (PowerShell)

.venv\Scripts\Activate.ps1


Windows (CMD)

.venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Application
python src/weather_gui.py

🖥️ Output

The GUI displays the following weather information:

City name

Temperature (°C)

Feels-like temperature

Weather description

Humidity (%)

Wind speed (m/s)

Users can also save the weather report as a .txt file.

⚠️ Notes & Limitations

Internet connection is required

API key must be valid

Application runs as a desktop program (not web-based)

Weather data accuracy depends on OpenWeatherMap API

🚀 Future Enhancements

5-day weather forecast

Weather condition icons

Sunrise and sunset times

Mobile or web-based version

Multi-country weather support



👩‍💻 Author

Akkasha Latif
PhD Researcher in Artificial Intelligence
