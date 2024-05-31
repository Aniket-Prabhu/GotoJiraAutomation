import requests
from api_Details import token

def fetch_data(api_url):
    try:
        
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.get(api_url, headers=headers, verify = False, auth =("v11vishalbidikar@gmail.com",token))
        response.raise_for_status()
        return (response.json())
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None