import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
city = 'Nairobi'
url =  f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'

response = requests.get(url)
data = response.json()

print(data)