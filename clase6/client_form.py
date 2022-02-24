import requests

url = "http://localhost:8880/form"

payload={'name': 'gus',
'email': 'gus@gmail.com',
'message': 'addasdasd'}



response = requests.post( url, data=payload)

print(response.text)
print(response.status_code)

print("Mensaje enviado" in response.text)