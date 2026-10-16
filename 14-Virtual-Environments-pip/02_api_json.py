import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url, timeout=10)
print("Status Code:", response.status_code)

response. raise_for_status()

user = response.json()

print("Full Data:", user)

print("Name:", user["name"])
print("Email:", user["email"])
print("City:", user["address"]["city"])