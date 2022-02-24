import requests
## localhost = ip  127.0.0.1
url = "http://localhost:7001/student"

students = [{
    "name": "Gustavo",
    "courses": 1
        },
    {
    "name": "Juan",
    "courses": 8
        },
    {
    "name": "pedro",
    "courses": 2
        },
           
]

for student in students:
    response = requests.post(url, json=student)
    print(response)

response = requests.get(url)
print(response)
print(response.status_code)
print(response.json())

response = requests.delete(f"{url}/1")
print(response)

response = requests.put(f"{url}/2", json={"name":"Agustin", "courses": 3})
print(response)

response = requests.get(url)
print(response)
print(response.status_code)
print(response.json())