import json

class Rates:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def getInfo(self):
        print(f"  - {self.name}: {self.value}")

def load_rates():
    with open('rates.json', 'r') as f:
        return json.load(f)

def map_rates():
    rates = load_rates()
    return [Rates(k, v) for k, v in rates.items()]

def display_rates(rates):
    print("\n-- Currency exchange rates --\n")
    for rate in rates:
        print(f"{rate.name}: {rate.value}")

def get_currency_choice(rates):
    available_currencies = [rate.name for rate in rates]
    while True:
        print("\n-- press 0 to escape --")
        currency_from = input("Choose a currency to exchange from (ex: USD): ").upper()
        if currency_from == "0":
            return None, None

        currency_to = input("Choose a currency to exchange to (ex: EUR): ").upper()
        if currency_to == "0":
            return None, None

        if currency_from in available_currencies and currency_to in available_currencies:
            if currency_from != currency_to:
                return currency_from, currency_to
            else:
                print("\nYou cannot exchange to the same currency!")
        else:
            print("\nInvalid currency. Please try again.\n")

def get_amount():
    while True:
        try:
            return float(input("How much?: "))
        except ValueError:
            print("\nEnter a valid number.")

def find_rate_value(rates, currency):
    for rate in rates:
        if rate.name == currency:
            return rate.value
    return None

def convert(amount, from_value, to_value):
    initial_amount = amount / from_value
    new_amount = initial_amount * to_value
    print(f"\nConverted amount: {new_amount:.2f}")

def main():
    while True:
        rates = map_rates()
        display_rates(rates)

        currency_from, currency_to = get_currency_choice(rates)
        if not currency_from or not currency_to:
            return

        amount = get_amount()

        currency_from_value = find_rate_value(rates, currency_from)
        currency_to_value = find_rate_value(rates, currency_to)

        convert(amount, currency_from_value, currency_to_value)

if __name__ == '__main__':
    main()
