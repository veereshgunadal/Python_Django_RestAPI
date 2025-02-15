import requests, json

a = {'name':'Virat Kohli', 'roll_no':1, 'age': 128, 'addr':'Dehli', 'ph_no':1234567890, 'department':'Style'}
b = json.dumps(a)

r = requests.put('http://127.0.0.1:8000/update1/1/', data = a)

print(r.status_code)
print(r.text)
print(r.json())
print(r.headers)