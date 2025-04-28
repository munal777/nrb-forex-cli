from api import NRBapi
from storage import Storage

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
            return True
        
        if force_refresh or not self.storage.is_data_fresh():
            # Try ro get fresh data from API
            api_data = self.api.fetch_latest_rates()

            if api_data:
                self.rates_data = api_data
                self.is_offline = False
                return True

        # Fall back to stored data   
        stored_data = self.storage.load_rates()
        if stored_data:
            self.rates_data = stored_data
            self.is_offline = True
            return True
        
        # Try loading from history as last resort
        history_data = self.storage.load_latest_from_history()
        if history_data:
            self.rates_data = history_data
            self.is_offline = True
            return True
            
        return False
    
