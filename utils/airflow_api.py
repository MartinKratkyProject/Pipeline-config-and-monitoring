import requests
from datetime import datetime, timezone

localhost = 'http://localhost:8080/'
api_endpoint = '/api/v2'
auth_endpoint = '/auth/token'

credentials = {
    'username': 'airflow',
    'password': 'airflow'
} # admin

credentials = {
    'username': 'airflow_user1',
    'password': 'airflow_user1'
} # airflow_user1

def get_jwt_token(url):
    auth = requests.post(url, json=credentials)
    token = auth.json()['access_token']

    return token

def get_dags(url):
    token = get_jwt_token(localhost + auth_endpoint)
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)

    return response

response = get_dags(localhost + api_endpoint + '/dags')

dags = response.json()['dags']


def trigger_dag(dag_id):    
    token = get_jwt_token(localhost + auth_endpoint)

    payload = {
        "conf": {},
        "logical_date": datetime.now(timezone.utc).isoformat()
    }

    print(datetime.now(timezone.utc).isoformat())

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    response = requests.post(
        localhost + api_endpoint + '/dags/' + dag_id + '/dagRuns', 
        json=payload, 
        headers=headers
    )

    return response

print("triggering dag")
print(trigger_dag('test_dag_1'))

