import requests 
from urllib.parse import urljoin
from pprint import pprint

def read_api_endpoint(endpoint = "/", base_url = "http://127.0.0.1:8000"):
    url = urljoin(base_url, endpoint)
    response = requests.get(url)
    
    return response


if __name__ == '__main__':
    pprint(read_api_endpoint("/api").json())