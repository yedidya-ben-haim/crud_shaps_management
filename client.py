import requests

new_shape = {
        "shape_type": "square",
        "side": 50
}

url = "http://127.0.0.1:8000/shapes"

r = requests.post(url, json=new_shape)

