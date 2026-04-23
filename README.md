# Weather App

A simple command-line weather application that fetches current weather information using the WeatherAPI.

## Features

- Get real-time weather data for any city
- Display temperature, weather condition, humidity, and wind speed
- Uses the WeatherAPI service for accurate weather data

## Requirements

- Python 3.7+
- requests
- python-dotenv

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "Weather App"
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API key:
```
API_KEY=your_weatherapi_key_here
```

Get your API key from [WeatherAPI.com](https://www.weatherapi.com/)

## Usage

Run the application:
```bash
python main.py
```

Enter a city name when prompted, and the app will display the current weather information.

## Example Output

```
Enter City: London
City: London
Temperature: 15.2°C
Condition: Partly cloudy
Humidity: 72%
Wind Speed: 12.5 kph
```

## License

MIT
