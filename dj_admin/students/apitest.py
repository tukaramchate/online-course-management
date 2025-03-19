import requests
from requests.auth import HTTPBasicAuth

def getAuth():
    url = 'http://127.0.0.1:8000/api/v2/students'
    username = 'lkendre2525'  
    password = 'Laxman@123'  
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:    
        print(response.json())
    else:
        print(f'Failed to fetch courses. Status code: {response.status_code}')
getAuth()
