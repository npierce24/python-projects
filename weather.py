import requests

API_KEY = "c1a43c92fc63bbbc25eb4de3b85cc851"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']['temp']-273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature*1.8+32, 'Fahrenheit')
else:
    print('An error occurred.')