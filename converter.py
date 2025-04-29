from api import NRBapi
from storage import Storage
import requests

class CurrencyConverter:
    """Core class for converting NPR to foreign currencies"""

    def __init__(self):
        self.api = NRBapi()
        self.storage = Storage()
        self.rates_data = None
        self.is_offline = False
    
    def load_rates(self, force_refresh=False):
        """
        Load exchange rates, first trying API then falling back to stored rates
        
        Args:
            force_refresh (bool): Force refresh from API even if stored data is fresh
            
        Returns:
            bool: True if rates were loaded successfully, False otherwise
        """
         
        # Check if we already have fresh data loaded
        if self.rates_data and not force_refresh:
            print("fresh data is already loaded")
            return True
        
        if force_refresh or not self.storage.is_data_fresh():
            # Try ro get fresh data from API
            print("calling fresh data if not fresh data...")
            api_data = self.api.fetch_latest_rates()

            try:
                if api_data:
                    self.rates_data = api_data
                    self.storage.save_rates(api_data)  # This saves to both current and history
                    self.is_offline = False
                    return True
            except Exception as e:
                print(f"Could not connect to NRB API: {e}")

        # Use stored data because we couldn't connect or because data is still fresh
        stored_data = self.storage.load_rates()
        if stored_data:
            print("calling fresh stored_data..")
            self.rates_data = stored_data
            self.is_offline = True
            return True
        
        # Try loading from history as last resort
        history_data = self.storage.load_latest_from_history()
        if history_data:
            print("calling history data...")
            self.rates_data = history_data
            self.is_offline = True
            return True
            
        return False
    
    def get_available_currencies(self):
        """
        Get list of available currencies
        
        Returns:
            list: List of currency code dictionaries
        """
        if not self.rates_data:
            print("get_available_currencies: load_rate()")
            self.load_rates()
        
        if not self.rates_data:
            return []
        
        currencies = []
        for rate in self.rates_data['rates']:
            currencies.append({
                'code': rate['code'],
                'name': rate['currency'],
                'unit': rate['unit']
            })
        
        return currencies

    def convert(self, amount, target_currency):
        """
        Convert NPR to target currency
        
        Args:
            amount (float): Amount in NPR
            target_currency (str): Target currency code
            
        Returns:
            dict: Conversion result or None if conversion failed
        """
        if not self.rates_data:
            if not self.load_rates():
                return None
                
        # Find the target currency in the rates data
        currency_data = None
        for rate in self.rates_data['rates']:
            if rate.get('code') == target_currency:
                currency_data = rate
                break
                
        if not currency_data:
            return None
            
        # Extract buying and selling rates and currency unit
        try:
            buying_rate = float(currency_data.get('buy', 0))
            selling_rate = float(currency_data.get('sell', 0))
            unit = int(currency_data.get('unit', 1))
            
            # Convert the amount, considering the unit
            # For buying rate: NPR to Foreign Currency
            # For selling rate: NPR to Foreign Currency
            converted_buying = (amount / buying_rate) * unit if buying_rate else 0
            converted_selling = (amount / selling_rate) * unit if selling_rate else 0
            
            return {
                'from_currency': 'NPR',
                'to_currency': target_currency,
                'amount': amount,
                'unit': unit,
                'buying_rate': buying_rate,
                'selling_rate': selling_rate,
                'converted_buying': converted_buying,
                'converted_selling': converted_selling,
                'updated_at': self.rates_data['updated_at'],
                'published_on': self.rates_data.get('published_on', ''),
                'is_offline': self.is_offline
            }
        except (ValueError, TypeError) as e:
            print(f"Error converting currency: {e}")
            return None
    
    def _check_internet_coonection(self):
        """
        Check if there is an active internet connection by trying to reach NRB
        
        Returns:
            bool: True if internet is available, False otherwise
        """
        try:
            requests.head("https://www.nrb.org.np", timeout=2)
            return True
        except requests.RequestException:
            return False