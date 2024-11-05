import os
from flask import Flask
from flask_cors import CORS  # to avoid cors error in frontend
# from services.monitoring import monitoring_services
from services.alert_management import alert_management_services
# from services.user import user_services
# from services.model_endpoint import model_endpoint_services
from dotenv import load_dotenv

load_dotenv()
IPADDRESSES_WHITELIST = os.getenv('IPADDRESSES_WHITELIST')

app = Flask(__name__)
app.secret_key = 'my_very_own_secret_key'  # Replace with a strong random key

CORS(app, resources={r"*": {"origins": IPADDRESSES_WHITELIST}}, supports_credentials=True)  # Allow all origins for API routes

# Register blueprints
# app.register_blueprint(monitoring_services)
app.register_blueprint(alert_management_services)
# app.register_blueprint(user_services)
# app.register_blueprint(model_endpoint_services)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5800)
