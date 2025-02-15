import requests, json

a = {'name':'Virat12', 'roll_no':1,'age':34,'addr':'Delhi','ph_no':1234567890,'department':'Style'}
b = json.dumps(a)

r = requests.post('http://127.0.0.1:8000/create/', data=a)

print(r.status_code)
print(r.text)
print(r.json())
