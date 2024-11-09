import requests

class CurrencyConvector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://v6.exchangerate-api.com/v6/39f5f995ebac2f246b4d6d90"

    def get_exchange_rate(self, from_currency, to_currency):
        url = f"{self.base_url}/latest/{from_currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "conversion_rates" in data and to_currency in data["conversion_rates"]:
                return data["conversion_rates"][to_currency]
            else:
                raise ValueError("Currency conversion not found.")
        else:
            raise ConnectionError("Failed to get data from API. Check the API key or network connection.")

    def convert_currency(self, amount, from_currency, to_currency):
        rate = self.get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount

if __name__ == "__main__":
    api_key = "39f5f995ebac2f246b4d6d90"
    converter = CurrencyConvector(api_key)

    try:
        from_currency = input("Enter the shipping currency code (For example, USD): ").upper()
        to_currency = input("Enter the appointment currency code (For example, EUR): ").upper()
        amount = float(input("Enter the amount to convert: "))

        result = converter.convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    except ValueError as e:
        print(f"Error: {e}")
    except ConnectionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")
