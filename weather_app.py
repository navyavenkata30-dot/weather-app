import requests

API_KEY = "026dc363d8a39e3e9b0e5b948407c97e"  # your API key here

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition.capitalize()}")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found. Please try again.")

def main():
    print("🌤 Weather App 🌤")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()

