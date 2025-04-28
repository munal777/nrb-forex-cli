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


obj = CurrencyConverter()
print(display_currencies(obj))