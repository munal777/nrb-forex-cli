import os
import json
import datetime

class Storage:

    def __init__(self):
        self.data_dir = os.path.expanduser("~/.nprconvert")
        self.data_file = os.path.join(self.data_dir, "rates.json")
        self.history_dir = os.path.join(self.data_dir, "history")
    
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if not os.path.exists(self.history_dir):
            os.makedirs(self.history_dir)

    
    def save_rates(self, rates_data):
        """
        Save exchange rates data to local storage
        
        Args:
            rates_data (dict): Exchange rate data from the API
        """

        # Save the latest data
        with open(self.data_file, 'w') as f:
            json.dump(rates_data, f, indent=2)

        # Also save to history with date in filename
        if rates_data and 'updated_at' in rates_data:
            date_str = rates_data['updated_at'].replace("-", "")

            history_file = os.path.join(self.history_dir, f"rates_{date_str}.json")

            if not os.path.exists(history_file):
                with open(history_file, 'w') as f:
                    json.dump(rates_data, f, indent=2)

    
    def load_rates(self):
        """
        Load exchange rates data from local storage
        
        Returns:
            dict: Exchange rate data or None if no saved data exists
        """
        if not os.path.exists(self.data_file):
            print("data_file exist.")
            return None
            
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading saved rates: {e}")
            return None
    
    def load_latest_from_history(self):
        """
        Load the most recent historical rate data when main data file is corrupted
        
        Returns:
            dict: Most recent exchange rate data or None if no history exists
        """

        try:
            history_files = os.listdir(self.history_dir)

            if not history_files:
                return None
            
            rate_files = [f for f in history_files if f.startswith('rates_')]

            if not rate_files:
                return None
                    
            # Sort by date (which is in the filename)
            latest_file = sorted(rate_files)[-1]

            with open(os.path.join(self.history_dir, latest_file), 'r') as f:
                return json.load(f)
            
        except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
            print(f"Error loading from history: {e}")
            return None
        
    
    def is_data_fresh(self, max_age_hours=24):
        """
        Check if the stored data is fresh enough to use
        
        Args:
            max_age_hours (int): Maximum age in hours to consider data as fresh
            
        Returns:
            bool: True if data is fresh, False otherwise
        """
        data = self.load_rates()
        if not data or 'timestamp' not in data:
            return False
            
        try:
            saved_time = datetime.datetime.fromisoformat(data['timestamp'])
            current_time = datetime.datetime.now()
            age = (current_time - saved_time).total_seconds() / 3600  # Age in hours
            
            return age <= max_age_hours
        except (ValueError, TypeError):
            return False