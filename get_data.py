import requests
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

city = "Irpin"

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if geo_data['results']:
    latitude = geo_data['results'][0]['latitude']
    longitude = geo_data['results'][0]['longitude']
else:
    print("City not found.")
    exit()

today = date.today()
week_ago = today - timedelta(days=7)
start_date = week_ago.isoformat()
end_date = today.isoformat()


weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"


weather_response = requests.get(weather_url)
weather_data = weather_response.json()
# print(weather_data)


daily_data = weather_data['daily']
df = pd.DataFrame({
    'date': daily_data['time'],
	'temperature_max': daily_data['temperature_2m_max'],
	'temperature_min': daily_data['temperature_2m_min']
})

df.date = pd.to_datetime(df.date)

# print(df)




# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['temperature_max'], marker='o', label='Max Temp')
plt.plot(df['date'], df['temperature_min'], marker='o', label='Min Temp')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title(f'{city} Weather - Past 7 Days')
plt.legend()

# Rotate x-axis labels for readability
# plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig(f'data/{city}_weather_chart.png')
plt.show()


if not os.path.exists('data'):
	os.makedirs('data')

df.to_csv(f'data/{city}_weather_data.csv', index=False)
print(f"Data saved to 'data/{city}_weather_data.csv' and plot saved as 'data/{city}_weather_chart.png'.")