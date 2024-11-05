import os
from loggers.logger import logger
from dotenv import load_dotenv

load_dotenv() 
ES_DB_URL = os.getenv('ES_DB_URL', 'localhost:5601') 

class InvestigationPanel(object):
    def __init__(self):
        self.db = ES_DB_URL

        self.collection_name = 'investigation_panels'  # collection name

        self.fields = {
            "start_date": "string",
            "end_date": "string",
            "investigation_panels": "string"
        }

    def select(self, investigation_panel):  # select investigation panel results
        try: 
            # Return database query
            return ""
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f'Error - Failed to select investigation panel results: {str(e)}')
