import requests

new_data = {"shape_type": "square",
            "side": 54}


url = "http://127.0.0.1:8000/shapes"

r = requests.post(url, json=new_data)

print(r.status_code)

