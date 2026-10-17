# Without error handling
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1",
    timeout=10
)

response.raise_for_status()

user = response.json()

print(user['name'])

# error handling with try Exception
url = "https://jsonplaceholder.typicode.com/users/1"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    user = response.json()

    print("Name:", user['name'])
    print("Email:", user['email'])

except requests.exceptions.Timeout:
    print("Error: Request time out.")

except requests.exceptions.HTTPError as error:
    print("HTTP Error:", error)

except requests.exceptions.ConnectionError:
    print("Error: Check your internet connection.")

except requests.exceptions.RequestException as error:
    print("Request error:", error)

except ValueError:
    print("Error: Invalid JSON Request.")