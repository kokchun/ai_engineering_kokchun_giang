import requests
from urllib.parse import urljoin
from pprint import pprint


def read_api_endpoint(endpoint="/", base_url="http://127.0.0.1:8000"):
    url = urljoin(base_url, endpoint)
    response = requests.get(url)

    return response


def post_api_endpoint(payload, endpoint="/", base_url="http://127.0.0.1:8000"):
    url = urljoin(base_url, endpoint)
    response = requests.post(url=url, json=payload)

    return response


if __name__ == "__main__":
    # pprint(read_api_endpoint("/api").json())
    payload = {
        "SepalLengthCm": 6,
        "SepalWidthCm": 3,
        "PetalLengthCm": 3.8,
        "PetalWidthCm": 1.2,
    }
    pprint(post_api_endpoint(payload=payload, endpoint="/api/predict").json())
