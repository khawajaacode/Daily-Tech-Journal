# simple_weather_analysis_url.py

import pandas as pd
import matplotlib.pyplot as plt

# URL of weather CSV file
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv"

# Load data from URL
df = pd.read_csv(url)

# Show first few rows
print("First 5 rows:")
print(df.head())

# Summary
print("\nAverage temperature:", df["Temp"].mean())
print("Maximum temperature:", df["Temp"].max())
print("Minimum temperature:", df["Temp"].min())

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Plot
plt.plot(df["Date"], df["Temp"], color="blue")
plt.title("Daily Minimum Temperatures")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
