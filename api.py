import requests
import json
from datetime import datetime

class NRBapi:
    """Class to handle all API interactions with Nepal Rastra Bank exchange rate API"""

    def __init__(self):
        self.api_url = "https://www.nrb.org.np/api/forex/v1/rates"

    def fetch_latest_rates(self):
        """
        Fetch latest exchange rates from NRB API
        
        Returns:
            dict: Exchange rate data or None if failed
        """

        try: 

            today = datetime.now().strftime("%Y-%m-%d")
            
            # Use query parameters to get today's rates
            params = {
                'from': today,
                'to': today,
                'per_page': 100,
                'page': 1
            }

            response = requests.get(self.api_url, params=params, timeout=5)
            response.raise_for_status()

            data = response.json()
            
            if (data.get('status', {}).get('code', {}) == 200 and
                data.get('data', {}).get('payload') and
                len(data['data']['payload']) > 0):

                first_payload = data['data']['payload'][0]
                
            return {
                'rates': self._standardize_rates(first_payload.get('rates', [])),
                'updated_at': first_payload.get('date', today),
                'published_on': first_payload.get('published_on', ''),
                'timestamp': datetime.now().isoformat()
            }
        

        except (requests.RequestException, json.JSONDecodeError) as e:
            print(f"Error fetching data from NRB API: {e}")
            return None
        
    def _standardize_rates(self, rates):
        """
        Convert the API's rate format to a standardized format for our application
        
        Args:
            rates (list): List of rate objects from the API
            
        Returns:
            list: Standardized rate objects
        """
        standardized = []

        for rate in rates:
            if 'currency' in rate and 'iso3' in rate['currency']:
                standardized.append({
                    'code': rate['currency']['iso3'],
                    'currency': rate['currency']['name'],
                    'unit': rate['currency']['unit'],
                    'buy': rate.get('buy', '0'),
                    'sell': rate.get('sell', '0')
                })
        
        return standardized

obj = NRBapi()
print(obj.fetch_latest_rates())

# today = datetime.today().strftime("%Y-%m-%d")

# CACHE_FILE = "rates_cache.json"
# NRB_API_URL = f"https://www.nrb.org.np/api/forex/v1/rates?from={today}&to={today}&per_page=100&page=1"

# def fetch_latest_rates():
#     try:
#         response = requests.get(NRB_API_URL)
#         data = response.json()
#         rates = data['data']['payload']
#         save_to_cache(rates)
#         return rates
#     except Exception as e:
#         return load_from_cache()


# def save_to_cache(rates):
#     with open(CACHE_FILE, 'w') as f:
#         json.dump(rates, f)

# def load_from_cache():
#     try:
#         with open(CACHE_FILE, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []
    

# def get_rate(currency_code, rates):
#     for rate in rates:
#         if rate['currency']['iso3'] == currency_code:
#             return rate
#         return None

# def convert_to_npr(amount, currency_code, rates):
#     rate = get_rate(currency_code, rates)
#     if rate:
#         pass