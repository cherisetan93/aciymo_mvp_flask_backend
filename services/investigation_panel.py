from flask import Blueprint, jsonify
from werkzeug.exceptions import BadRequest, Unauthorized, Forbidden, NotFound, InternalServerError, ServiceUnavailable, GatewayTimeout
from models import investigation_panel  # call model file
from loggers.logger import logger

investigation_panel = investigation_panel.InvestigationPanel()
investigation_panel_services = Blueprint('investigation_panel_apis', __name__)

# Investigation Panel Routes
# Sample written to be modified.
@investigation_panel_services.route('/investigation_panels/', methods=['GET'])
def get_investigation_panels():
    try:
        # Successfully return data
        response = jsonify(investigation_panel.select({}))
        logger.info('Response 200: Successfully retrieve investigation_panel information.')
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
