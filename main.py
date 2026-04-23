import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
city = input("Enter City: ")
url =  f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'

response = requests.get(url)
data = response.json()

if "error" in data:
    print(f"Error: {data['error']['message']}")
else:
	print(f"City: {data['location']['name']}")
	print(f"Temperature: {data['current']['temp_c']}°C")
	print(f"Condition: {data['current']['condition']['text']}")
	print(f"Humidity: {data['current']['humidity']}%")
	print(f"Wind Speed: {data['current']['wind_kph']} kph")