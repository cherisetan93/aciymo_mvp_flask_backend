from flask import Blueprint, request, jsonify
from werkzeug.exceptions import BadRequest, Unauthorized, Forbidden, NotFound, InternalServerError, ServiceUnavailable, GatewayTimeout
from models import alert_management  # call model file
from loggers.logger import logger

alert_management = alert_management.AlertManagement()
alert_management_services = Blueprint('alert_management_apis', __name__)

# Alert Management Routes

# API Service that provides Overview of Plant-Process Alerts (User Story 1)
@alert_management_services.route('/api/v0/summary-of-all-plant-process-alerts/', methods=['GET'])
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


# API Service that provides Alert-Types Summary for given Process Number (User Story 2)
@alert_management_services.route('/api/v0/summary_of_alerts_per_plant_process/<int:process_number>', methods=['GET'])
def get_summary_of_given_plant_process_alerts(process_number):
    try:
        # Successfully return data. (Once connection with ES is ready)
        # response = jsonify(alert_management.count_process_alerts_types(process_number))

        # Hardcoded dummy response back from ES.
        output = {
                    "host_alerts": 1,
                    "unauthorised_commands": 1,
                    "faults": 1,
                    "baseline_deviations": 1
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
    

# API Service that provides Alert Listings Per Process (User Story 3)
@alert_management_services.route('/api/v0/alerts-per-plant-process/<int:process_number>', methods=['GET'])
def get_alert_listing_per_process(process_number):
    try:
        # Successfully return data. (Once connection with ES is ready)
        # response = jsonify(alert_management.select_process_alerts_types(process_number))

        # Hardcoded dummy response back from ES.
        output = {
                "host_alerts": [{
                            "status": "new",
                            "date_start":
                                "2024-01-30T16:21:06.405Z",
                            "error_code": [
                                "OSLOG"
                            ],
                            "error_message": 
                                "Anomolous log detected"
                            ,
                            "event_id": [
                                "9d2a1b8bf3717386effb6cc78bd3e8bb"
                            ],
                            "hostname": 
                                "SUTD_ITrust_PC"
                            ,
                            "message": 
                                "An account was logged off.\n\nSubject:\n\tSecurity ID:\t\tS-1-5-7\n\tAccount Name:\t\tANONYMOUS LOGON\n\tAccount Domain:\t\tNT AUTHORITY\n\tLogon ID:\t\t0x2c00ec678\n\nLogon Type:\t\t\t3\n\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer."
                            ,
                            "mitre_attack_tactic:technique": 
                                "tbc"
                            ,
                            "_id": "hXLHwI4Bk9ck9hpaixC8",
                            "_index": "alert-os_log_detection_2024-01-30",
                            "_score": 0
                            }],

                "unauthorised_commands": [{
                            "status": "new",
                            "date_end": 
                                "2024-01-30T16:05:04.738Z"
                            ,
                            "date_start": 
                                "2024-01-30T16:05:04.738Z"
                            ,
                            "dest-ip": 
                                "192.168.1.30"
                            ,
                            "error_code": 
                                "CMD"
                            ,
                            "error_message": 
                                "Unauthorized command detected"
                            ,
                            "process_number": 
                                "1"
                            ,
                            "process_number.keyword": 
                                "1"
                            ,
                            "source-ip": 
                                "192.168.1.201"
                            ,
                            "source-process": 
                                "HMI/Engineering Work Station"
                            ,
                            "source-process.keyword": 
                                "HMI/Engineering Work Station"
                            ,
                            "_id": "R3LCwI4Bk9ck9hpawhCB",
                            "_index": "alert-abnormal_command_2024-01-30",
                            "_score": 0
                            }],
                "faults": [{
                        "status": "new",
                        "date_end": 
                            "2024-05-08T06:43:12.000Z"
                        ,
                        "date_start": 
                            "2024-05-08T06:43:12.000Z"
                        ,
                        "equipment": 
                            "LIT101.Pv"
                        ,
                        "error_code": 
                            "FAULT"
                        ,
                        "error_message": 
                            "Unusual change in sensor value detected"
                        ,
                        "values": 
                            792.86646
                        ,
                        "_id": "hczxVo8Bkfn1kX2wNxZH",
                        "_index": "alert-fault_detection_2024-05-08",
                        "_score": 0
                        }],
                "baseline_deviations": [{
                        "status": "new",
                        "date_end": 
                            "2024-01-30T16:15:48.000Z",
                        "date_start": 
                            "2024-01-30T16:10:34.000Z",
                        "error_code": 
                            "P5_PBAD",
                        "error_message": 
                            "Deviation from plant baseline detected",
                        "process_number":
                            "1",
                        "_id": "JXK6wI4Bk9ck9hpa_hDz",
                        "_index": "alert-plant_baseline_2024-01-30",
                        "_score": 1
                        }]
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