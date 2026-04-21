import requests

def get_weather(city):
    """Fetch weather using wttr.in - no API key, no signup needed"""
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url)
        data = response.json()

        if 'current_condition' in data:
            current = data['current_condition'][0]
            print("\n--- Weather Report ---")
            print(f"City: {city.title()}")
            print(f"Temperature: {current['temp_C']}°C")
            print(f"Condition: {current['weatherDesc'][0]['value']}")
            print(f"Humidity: {current['humidity']}%")
            print(f"Feels Like: {current['FeelsLikeC']}°C")
        else:
            print("Error: City not found. Try another city name.")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def get_crypto(coin):
    """Fetch crypto price using CoinGecko API - no API key needed"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin.lower()}&vs_currencies=usd,inr&include_24hr_change=true"

    try:
        response = requests.get(url)
        data = response.json()

        if coin.lower() in data:
            print("\n--- Crypto Price ---")
            print(f"Coin: {coin.title()}")
            print(f"Price USD: ${data[coin.lower()]['usd']}")
            print(f"Price INR: ₹{data[coin.lower()]['inr']}")
            print(f"24h Change: {data[coin.lower()]['usd_24h_change']:.2f}%")
        else:
            print(f"Error: Coin '{coin}' not found. Try 'bitcoin', 'ethereum', 'dogecoin'")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def get_news(query):
    """Fetch news using NewsData.io - with API key"""
    API_KEY = "pub_c7d8d12e146f44ba82fac8f5e8e93807"  # Quotes added
    url = f"https://newsdata.io/api/1/news?apikey={API_KEY}&q={query}&language=en&size=5"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get('status') == 'success' and data.get('results'):
            print(f"\n--- Top 5 News for '{query}' ---")
            for i, article in enumerate(data['results'][:5], 1):
                print(f"\n{i}. {article['title']}")
                print(f" Source: {article.get('source_id', 'Unknown')}")
                print(f" URL: {article.get('link', 'N/A')}")
        else:
            print(f"Error: No news found for '{query}' or API limit reached")
            print(f"Message: {data.get('message', '')}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def main():
    print("API Integration Tool - Weather / Crypto / News")
    print("No signup needed for any API")
    print("1. Weather\n2. Crypto\n3. News")

    choice = input("\nEnter choice (1/2/3): ")

    if choice == '1':
        city = input("Enter city name: ")
        get_weather(city)
    elif choice == '2':
        coin = input("Enter coin name (e.g., bitcoin, ethereum): ")
        get_crypto(coin)
    elif choice == '3':
        topic = input("Enter news topic to search: ")
        get_news(topic)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()