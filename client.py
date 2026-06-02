import requests

new_shape = {
        "side": 70
}

url = "http://127.0.0.1:8000/shapes/1"

r = requests.put(url, json=new_shape)

