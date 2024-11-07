from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, Unauthorized, Forbidden, NotFound, InternalServerError, ServiceUnavailable, GatewayTimeout
from models import alert_management  # call model file
from loggers.logger import logger

alert_management = alert_management.AlertManagement()
alert_management_us1_services = Blueprint('alert_management_us1_apis', __name__)

# Alert Management Routes

# API Service that provides Overview of Plant-Process Alerts (User Story 1)
@alert_management_us1_services.route('/api/v0/summary-of-all-plant-process-alerts/', methods=['GET'])
def get_summary_of_all_plant_process_alerts():
    try:
        # Successfully return data. (Once connection with ES is ready)
        # response = jsonify(alert_management.count_summary_of_process_alerts())

        # Hardcoded dummy response back from ES.
        output = {
                    "process_1": 4,
                    "process_2": 0,
                    "process_3": 3,
                    "process_4": 0,
                    "process_5": 0,
                    "process_6": 0
                }
        response = jsonify(output)
        logger.info('Response 200: Successfully retrieve alert management information.')
        return response, 200
    except BadRequest:
        # Handle 400 Bad Request error
        logger.error('Response 400: Bad Request error')
        return jsonify({'error': 'Bad Request'}), 400
    except Unauthorized:
        # Handle 401 Unauthorized error
        logger.error('Response 401: Unauthorized error')
        return jsonify({'error': 'Unauthorized'}), 401
    except Forbidden:
        # Handle 403 Forbidden error
        logger.error('Response 403: Forbidden error')
        return jsonify({'error': 'Forbidden'}), 403
    except NotFound:
        # Handle 404 Not Found error
        logger.error('Response 404: Not Found error')
        return jsonify({'error': 'Not Found'}), 404
    except InternalServerError:
        # Handle 500 Internal Server Error
        logger.error('Response 500: Internal Server Error')
        return jsonify({'error': 'Internal Server Error'}), 500
    except ServiceUnavailable:
        # Handle 503 Service Unavailable error
        logger.error('Response 503: Service Unavailable error')
        return jsonify({'error': 'Service Unavailable'}), 503
    except GatewayTimeout:
        # Handle 504 Gateway Timeout error
        logger.error('Response 504: Gateway Timeout error')
        return jsonify({'error': 'Gateway Timeout'}), 504
    except Exception as e:
        # Catch any other unexpected errors
        logger.error(f'Response 500: {str(e)}')
        return jsonify({'error': str(e)}), 500
