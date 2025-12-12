"""
Weather Checker - Tkinter GUI (Python)
(Modified version: confined to Pakistan only, with Pakistan time zone)
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
import threading
from datetime import datetime, timedelta  # ✅ Added timedelta here

API_KEY = "8077a0d186d0cbe785d15245b682e70f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# === Helper: fetch weather (runs in background thread) ===
def fetch_weather(city, callback):
    try:
        params = {"q": f"{city},PK", "appid": API_KEY, "units": "metric"}
        resp = requests.get(BASE_URL, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.json()

            # Restrict to Pakistan
            if data.get("sys", {}).get("country") != "PK":
                callback(success=False, error="Only Pakistani cities are supported.")
                return

            callback(success=True, data=data)
        else:
            callback(success=False, error=f"API returned status {resp.status_code}: {resp.text}")
    except Exception as e:
        callback(success=False, error=str(e))

# === GUI ===
class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pakistan Weather Checker")
        self.geometry("460x360")
        self.resizable(False, False)
        self.create_widgets()
        self.last_report = None

    def create_widgets(self):
        lbl = ttk.Label(self, text="Weather Checker (Pakistan Only)", font=("Segoe UI", 16, "bold"))
        lbl.pack(pady=(12, 6))

        frame = ttk.Frame(self)
        frame.pack(fill="x", padx=12)

        city_lbl = ttk.Label(frame, text="Enter Pakistani city name:")
        city_lbl.grid(row=0, column=0, sticky="w")
        self.city_var = tk.StringVar()
        city_entry = ttk.Entry(frame, textvariable=self.city_var, width=30)
        city_entry.grid(row=0, column=1, sticky="w")
        city_entry.bind("<Return>", lambda ev: self.on_check())

        self.check_btn = ttk.Button(frame, text="Check Weather", command=self.on_check)
        self.check_btn.grid(row=0, column=2, padx=(8, 0))

        # Result area
        self.result_box = tk.Text(self, height=10, width=52, state="disabled", wrap="word")
        self.result_box.pack(padx=12, pady=(12, 4))

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=(6, 0))
        save_btn = ttk.Button(btn_frame, text="Save Report", command=self.save_report)
        save_btn.grid(row=0, column=0, padx=6)
        clear_btn = ttk.Button(btn_frame, text="Clear", command=self.clear_result)
        clear_btn.grid(row=0, column=1, padx=6)
        quit_btn = ttk.Button(btn_frame, text="Quit", command=self.quit)
        quit_btn.grid(row=0, column=2, padx=6)

        note = ttk.Label(
            self,
            text="Note: This version only supports cities within Pakistan.",
            font=("Segoe UI", 8),
        )
        note.pack(pady=(8, 0))

    def on_check(self):
        city = self.city_var.get().strip()
        if not city:
            messagebox.showinfo("Input needed", "Please enter a city name.")
            return
        self.check_btn.config(state="disabled")
        self.append_result(f"🔎 Fetching weather for '{city}, Pakistan'...")

        thread = threading.Thread(target=fetch_weather, args=(city, self.after_fetch))
        thread.daemon = True
        thread.start()

    def after_fetch(self, success, data=None, error=None):
        self.after(0, self._after_fetch_gui, success, data, error)

    def _after_fetch_gui(self, success, data, error):
        self.check_btn.config(state="normal")
        if not success:
            self.append_result(f"❌ Error: {error}")
            return
        try:
            name = data.get("name")
            country = data.get("sys", {}).get("country")
            temp = data["main"]["temp"]
            feels = data["main"].get("feels_like")
            humidity = data["main"]["humidity"]
            wind = data.get("wind", {}).get("speed")
            desc = data["weather"][0]["description"].title()

            # === Pakistan Time Conversion === ✅
            utc_dt = datetime.utcfromtimestamp(data.get("dt", 0))
            pakistan_dt = utc_dt + timedelta(hours=5)  # Pakistan Standard Time (UTC+5)

            utc_str = utc_dt.strftime("%Y-%m-%d %H:%M UTC")
            pakistan_str = pakistan_dt.strftime("%Y-%m-%d %I:%M %p (Pakistan Time)")

            # === Report Lines ===
            report_lines = [
                f"Weather report for {name}, {country}",
                f"Time (UTC): {utc_str}",
                f"Local Time: {pakistan_str}",  # ✅ Added Pakistan time
                f"Description: {desc}",
                f"Temperature: {temp} °C",
                f"Feels like: {feels} °C",
                f"Humidity: {humidity} %",
                f"Wind speed: {wind} m/s",
            ]
            report = "\n".join(report_lines)
            self.last_report = report
            self.append_result(report)
        except Exception as ex:
            self.append_result(f"❌ Failed to parse data: {ex}")

    def append_result(self, text):
        self.result_box.config(state="normal")
        self.result_box.insert("end", text + "\n\n")
        self.result_box.see("end")
        self.result_box.config(state="disabled")

    def save_report(self):
        if not self.last_report:
            messagebox.showinfo("Nothing to save", "No report to save. Please fetch weather first.")
            return
        fpath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")], title="Save report as...")
        if not fpath:
            return
        try:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(self.last_report)
            messagebox.showinfo("Saved", f"Report saved to:\n{fpath}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

    def clear_result(self):
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", "end")
        self.result_box.config(state="disabled")
        self.last_report = None


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
