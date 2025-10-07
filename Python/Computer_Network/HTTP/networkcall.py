import requests

response = requests.get('https://api.github.com/events')
print(response.status_code)
print(response.links)
print(response.headers)
print(response.request)
# print(response.json()) # For JSON responses