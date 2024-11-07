import os
from flask import Flask
from flask_cors import CORS  # to avoid cors error in frontend
from services.us1_summary_of_all_plant_process_alerts import alert_management_us1_services
from services.us2_summary_of_alerts_per_plant_process import alert_management_us2_services
from services.us3_alerts_per_plant_process import alert_management_us3_services
from dotenv import load_dotenv

load_dotenv()
IPADDRESSES_WHITELIST = os.getenv('IPADDRESSES_WHITELIST')

app = Flask(__name__)
app.secret_key = 'my_very_own_secret_key'  # Replace with a strong random key

CORS(app, resources={r"*": {"origins": IPADDRESSES_WHITELIST}}, supports_credentials=True)  # Allow all origins for API routes

# Register blueprints
app.register_blueprint(alert_management_us1_services)
app.register_blueprint(alert_management_us2_services)
app.register_blueprint(alert_management_us3_services)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5800)
