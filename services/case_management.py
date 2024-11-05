from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, Unauthorized, Forbidden, NotFound, InternalServerError, ServiceUnavailable, GatewayTimeout
from models import case_management  # call model file
from loggers.logger import logger

case_management = case_management.CaseManagement()
case_management_services = Blueprint('case_management_apis', __name__)

# Case Management routes
# Sample written to be modified.
@case_management_services.route('/case_managements/', methods=['GET'])
def get_case_managements():
    try:
        # Successfully return data
        response = jsonify(case_management.select({}))
        logger.info('Response 200: Successfully retrieve case_management information.')
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

@case_management_services.route('/case_managements', methods=['PUT'])
def update_case_managements():
    try:
        # Successfully update a new record to the data.
        if request.method == "PUT":
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            response = case_management.update({'start_date': start_date, 'end_date': end_date})
            logger.info('Response 201: Successfully updated a record case_management.')
            return response, 201
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
