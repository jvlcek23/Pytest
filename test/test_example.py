import requests
import os
from pprint import pprint
from test_runner import env_vars

print("Script started")
print(env_vars)

def test_github_api():
    url = "https://api.github.com"
    
    response = requests.get(url)
    
    assert response.status_code == 200, f"expected 200 but got {response.status_code}"
    
    # pprint(response.json())

# test_github_api()

