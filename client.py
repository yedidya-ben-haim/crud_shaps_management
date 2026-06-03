import requests

new_data = {"side": -10}


url = "http://127.0.0.1:8000/shapes/1"

r = requests.put(url, json=new_data)

print(r.status_code)
print(r.text)

