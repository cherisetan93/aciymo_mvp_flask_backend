import os
from loggers.logger import logger
from dotenv import load_dotenv

load_dotenv() 
ES_DB_URL = os.getenv('ES_DB_URL', 'localhost:5601') 

# Database Query fr Alert Management
# Sample written to be modified.
class AlertManagement(object):
    def __init__(self):
        self.db = ES_DB_URL

        self.collection_name = 'alert_managements'  # collection name

        self.fields = {
            "start_date": "string",
            "end_date": "string",
            "alert_managements": "string",
            "alert_processes_counts": "integer"
        }

    def count_summary_of_process_alerts(self):  # Overview of Plant-Process Alerts (User Story 1) - count all process alerts
        try: 
            # Return database query
            return ""
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f'Error - Failed to count all process alerts: {str(e)}')

    def count_process_alerts_types(self, process_number):  # Alert-Types Summary for given Process Number (User Story 2) - count process alerts type
        try: 
            # Return database query
            return ""
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f'Error - Failed to count process alerts type: {str(e)}')

    def select_process_alerts_types(self, process_number):  # Alert Listings Per Process (User Story 3) - select process alerts type
        try: 
            # Return database query
            return ""
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f'Error - Failed to count process alerts type: {str(e)}')

    