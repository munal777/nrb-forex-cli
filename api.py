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

