import argparse
import sys
from converter import CurrencyConverter
from InquirerPy import inquirer

def display_currencies(converter):
    """Display available currencies"""
    currencies = converter.get_available_currencies()

    if not currencies:
        print("Failed to retrieve currency list. Check your internet connection.")
        return
    
    print("\nAvailable currencies:")
    print("-" * 40)
    print(f"{'Code':<10} {'Currency':<40}")
    print("-" * 40)
    
    for currency in currencies:
        print(f"{currency['code']:<10} {currency['name']:<40}")
    print("-" * 40)

def choose_currency_menu(converter):
    currencies = converter.get_available_currencies()

    if not currencies:
        print("❌ Failed to fetch currencies.")
        return
    
    choices = [f"{c['code']} - {c['name']}" for c in currencies]

    selected = inquirer.select(
        message="Select a currency",
        choices=choices,
        pointer="→",
        style={"pointer": "#00ffcc", "question": "bold"},
    ).execute()
    
    selected_code = selected.split(" - ")[0]

    result = converter.convert()

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
        print(f"Last updated: {result['updated_at']}")
        print(f"Last published: {result['published_on']}")
    else:
        print("✅ Using current online data")
        print(f"Updated: {result['updated_at']}")
        print(f"Published: {result['published_on']}")

    print("-" * 60)
    print(f"Amount: {amount:.2f} NPR")
    print(f"Target Currency: {result['to_currency']} (per {result['unit']} unit{'s' if result['unit'] > 1 else ''})")
    print("-" * 60)
    print(f"Buying Rate: {result['unit']} {result['to_currency']} = {result['buying_rate']:.4f} NPR")
    print(f"Selling Rate: {result['unit']} {result['to_currency']} = {result['selling_rate']:.4f} NPR")
    print("-" * 60)
    print(f"Converted Amount (Buying): {result['converted_buying']:.4f} {result['to_currency']}")
    print(f"Converted Amount (Selling): {result['converted_selling']:.4f} {result['to_currency']}")




def main():
    """Main entry point for CLI"""
    parser = argparse.ArgumentParser(
        description="Convert NPR to foreign currencies using Nepal Rastra Bank exchange rates"
    )

    parser.add_argument(
        "-l", "--list",
        action="store_true",
        help="List all available currencies"
    )

    parser.add_argument(
        "-a", "--amount",
        type=float,
        help="Amount in NPR to convert"
    )

    parser.add_argument(
        "-t", "--to",
        type=str,
        help="Target currency code (e.g., USD, EUR, INR)"
    )

    parser.add_argument(
        "-f", "--force-refresh",
        action="store_true",
        help="Force refresh from the NRB API instead of using cached data"
    )

    args = parser.parse_args()
    converter = CurrencyConverter()

    if args.force_refresh:
        print("🔄 Forcing refresh from NRB API...")
        converter.load_rates(force_refresh=True)
        return
    
    if args.list:
        display_currencies(converter)
        return
    
    if args.amount is not None and args.to:
        convert_currency(converter, args.amount, args.to.upper())
        return

    # If no valid options were provided, show help
    parser.print_help()

if __name__ == "__main__":
    main()

# obj = CurrencyConverter()
# print(display_currencies(obj))
# result = convert_currency(obj, 10, "USD")
