import requests

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

for dag in dags:
    print(dag['dag_id'])
    print(dag['description'])

