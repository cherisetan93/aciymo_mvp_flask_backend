import os
from loggers.logger import logger
from dotenv import load_dotenv

load_dotenv() 
ES_DB_URL = os.getenv('ES_DB_URL', 'localhost:5601') 

class CaseManagement(object):
    def __init__(self):
        self.db = ES_DB_URL

        self.collection_name = 'case_management'  # collection name

        self.fields = {
            "start_date": "string",
            "end_date": "string",
        }

        # Fields required for UPDATE
        self.update_required_fields = ["start_date", "end_date"]

        # Fields optional for UPDATE
        self.update_optional_fields = []

    def select(self, case_management):  # find all
        try: 
            return self.db.select(case_management, self.collection_name)
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f'Error - Failed to select case management: {str(e)}')

    def update(self, case_management):
        try: 
            self.validator.validate(case_management, self.fields, self.update_required_fields, self.update_optional_fields)
            return self.db.update(case_management, self.collection_name)
        except Exception as e:
            # Catch any other unexpected errors
            logger.error(f'Error - Failed to update case management: {str(e)}')
