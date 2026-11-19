def greet(name, greeting="hello"):
    print(f"{greeting}, {name}!")
print(greet("alice"))
print(greet("bob", "hi"))
print(greet("charlie"))
print(greet("david", "hello"))
def list1():
    print("hello world")
a = [1,2,3,4,5]
print(a)
for i in a:
    print(i)

try:
    list1()
except:
    print("error")
nums = [1, 2, 3, 4, 5]

# 基本形式：[表达式 for 变量 in 可迭代对象]
squares = [n * n for n in nums]
print(squares)         # [1, 4, 9, 16, 25]

# 带条件
evens = [n for n in nums if n % 2 == 0]
print(evens)           # [2, 4]

# 对字典做
users = [{"name": "a", "age": 10}, {"name": "b", "age": 20}]
names = [u["name"] for u in users]
print(names)           # ['a', 'b']

# 带 if-else 的表达式（注意 if-else 在 for 前面）
labels = ["even" if n % 2 == 0 else "odd" for n in nums]
print(labels)
class apiclient:
    def __init__(self, url, headers = {}) -> None:
        self.url = url
        self.headers = headers
    def set_token(self, token):
        self.headers["Authorization"] = f"Bearer {token}"
    def call(self, endpoint, method="GET", data=None):
        url = f"{self.url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=data)
        return response.json()
c = apiclient("https://api.example.com", {"Content-Type": "application/json"})
c.set_token("123456")
print(c.call("users"))
    



