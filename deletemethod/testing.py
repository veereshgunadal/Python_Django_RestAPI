import requests, json

r = requests.delete('http://127.0.0.1:8000/delete/1/')

print(r.status_code)
print(r.text)
#print(r.json())