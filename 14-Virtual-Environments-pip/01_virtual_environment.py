import requests

response = requests.get("https://example.com", timeout=10)

print("Status code:", response.status_code)
print("Respose successful:", response.ok)
print("Website content:")
print(response.text[:300])