import requests, json

req = {'name':'Shreyas','roll_no':4,'age':30,'addr':'Mumbai','ph_no':'1234567a890','department':'Normal'}
json_data = json.dumps(req)

r = requests.post('http://127.0.0.1:8000/createstudentr/', data = json_data)

print(r.status_code)
print(r.text)
print(r.json())