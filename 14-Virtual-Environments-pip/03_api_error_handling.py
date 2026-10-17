# Without error handling
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
    timeout=10
)

response.raise_for_status()

user = response.json()

print(user['name'])

