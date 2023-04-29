import requests

api_key = "64cf35cf6622ee235bb6f30547f409e0"
city = "London"
country_code = "UK"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Country: {country_code}\nLocation: {city}\nTemperature: {data['main']['temp']}°C")
else:
    print("Error getting weather data.")
    print(response.text) 