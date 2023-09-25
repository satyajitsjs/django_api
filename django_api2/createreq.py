import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data ={
    "name" : "Satyajit",
    "email":"satyajit@gail.com",
    "password":"Satya$143"
}

json_data = json.dumps(data)

req = requests.post(url = URL , data = json_data)

newdata = req.json()

print(newdata)