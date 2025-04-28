import argparse
import sys
from converter import CurrencyConverter

def display_currencies(converter):
    """Display available currencies"""
    currencies = converter.get_available_currencies()

    if not currencies:
        print("Failed to retrieve currency list. Check your internet connection.")
        return
    
    print("\nAvailable currencies:")
    print("-" * 60)
    print(f"{'Code':<10} {'Currency':<40} {'Unit':<10}")
    print("-" * 60)
    
    for currency in currencies:
        print(f"{currency['code']:<10} {currency['name']:<40} {currency['unit']:<10}")


def convert_currency(converter, amount, target):
    """Convert and display currency conversion"""
    result = converter.convert(amount, target)

    if not result:
        print(f"Failed to convert {amount} NPR to {target}.")
        print("Please check your internet connection or try again later.")
        return
    print(result["to_currency"])

    print("\nCurrency Conversion Result")
    print("-" * 60)
    if result['is_offline']:
        print("⚠️  USING OFFLINE DATA - rates may not be current")

    print(f"Amount: {amount:.2f} NPR")
    print(f"Target Currency: {result['to_currency']} (per {result['unit']} unit{'s' if result['unit'] > 1 else ''})")
    print(f"Rates as of: {result['updated_at']}")
    print(f"Published on: {result['published_on']}")
    print("-" * 60)
    print(f"Buying Rate: {result['unit']} {result['to_currency']} = {result['buying_rate']:.4f} NPR")
    print(f"Selling Rate: {result['unit']} {result['to_currency']} = {result['selling_rate']:.4f} NPR")
    print("-" * 60)
    print(f"Converted Amount (Buying): {result['converted_buying']:.4f} {result['to_currency']}")
    print(f"Converted Amount (Selling): {result['converted_selling']:.4f} {result['to_currency']}")


obj = CurrencyConverter()
# print(display_currencies(obj))
result = convert_currency(obj, 10, "INR")
