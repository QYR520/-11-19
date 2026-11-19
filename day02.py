import json
from os import name
import requests
from urllib3 import response

data = {"name": "a", "age": 18}
dump = json.dumps(data)
print(dump)
load = json.loads(dump)
print(load)
dump = json.dumps(load)
print(dump)
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)

response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)
print(response.status_code)
print(response.elapsed.total_seconds())
print(response.text[:200])
data = response.json()
name = data["name"]
print(name)
email = data["email"]
print(email)
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
with open("data.json", "r") as f:
    save_data = json.load(f)
    print(save_data)
print(save_data["address"]["city"])

# params 用法：GET 参数放查询串，不放请求体
r2 = requests.get(
    "https://jsonplaceholder.typicode.com/comments",
    params={"postId": 1},
    timeout=5,
)
print("comments?postId=1 返回条数:", len(r2.json()))
