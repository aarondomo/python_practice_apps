import requests

def get_response(url):
    response = requests.get(url)
    if (response.ok):
        return response
    else:
        return None