import requests

url = "http://www.youtube.com.com"
dados = requests.get(url)
print(dados)
print(dados.headers)
print(dados.content)
print(dados.json)
print(dados.text)