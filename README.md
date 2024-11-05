# ACIYMO MVP Product Flask Backend

## CREATE [virtual environment] AND INSTALL PACKAGES:
```sh
pip install -r requirements.txt
```
## CHANGE ENVIRONMENT VARIABLES (DEVELOPMENT / PRODUCTION):
.env 

## RUN DIRECT PYTHON BACKEND:
```sh
python app.py 
```

## RUN DOCKER IMAGE RUN BACKEND:
```sh
docker-compose up --build
```

## LOGS FILES (DATE / TIME / LOG STATUS LEVEL / INFORMATION):
Path (loggers/logs)
Eg. File - app_2024_11_04.log
2024-11-04 16:55:56,655 - INFO - Response 200: Successfully retrieve alert_status information.

## FLASK BACKEND MICROSERVICES 
#### List Models (Queries from Database)

#### List of all Routes (API Services)
| Request | Endpoint |  Details |
| --- | --- | --- |
| `GET` | `http://127.0.0.1:5800/api/v0/summary-of-all-plant-process-alerts/`| Overview of Plant-Process Alerts|
| `GET` | `http://127.0.0.1:5800/api/v0/summary-of-given-plant-process-alerts/<int:process_number>`| Alert-Types Summary for given Process Number|
| `GET` | `http://127.0.0.1:5800/api/v0/alerts-per-plant-process/<int:process_number>`| API Service that provides Alert Listings Per Process

