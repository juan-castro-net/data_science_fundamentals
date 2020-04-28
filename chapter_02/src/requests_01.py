import requests
import json

def show_response(response):
	print("Status code: ", response.status_code)

	json_response = response.json()
	data = json_response['data']
	user = data['usuario']
	email = data['correo']

	print("Printing Post JSON data")
	print(data)
	print("Usuario: " + user)
	print("Correo: " + email)


theUrl = "http://localhost:5000"

print()
print("--- Method Post 1 ---")
data = {'user':'Sofia Perdomo',
		'email':'sofia.perdomo@gmail.com'}
response = requests.post(theUrl, json=data)
show_response(response)

print()
print("--- Method Post 2 ---")
data = {'user':'Jorge Arevalo',
		'email':'jorge.arevalo@gmail.com'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(theUrl,
                         data=json.dumps(data),
                         headers=headers)
show_response(response)

print()
print("--- Method Get (user list) ---")
theUrl = "http://localhost:5000/list"
response = requests.get(theUrl)
print("Status code: ", response.status_code)
json_items = response.json()
print(json_items)
for item in json_items:
	print("user:", item['usuario'], "email:", item['correo'])