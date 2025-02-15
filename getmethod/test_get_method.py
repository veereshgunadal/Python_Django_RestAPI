import requests,json

r = requests.get('http://127.0.0.1:8000/htmlstring')

print(r.status_code)
print(r.text)
#print(r.json())

r = requests.get('http://127.0.0.1:8000/htmltag')

print(r.status_code)
print(r.text)
#print(r.json())

r = requests.get('http://127.0.0.1:8000/httpjson')

print(r.status_code)
print(r.text)
print(r.json())

r = requests.get('http://127.0.0.1:8000/json')

print(r.status_code)
print(r.text)
print(r.json())