import requests


get = requests.get("https://github.com/henrique15775/AindaNaoSei")
print(get._content)