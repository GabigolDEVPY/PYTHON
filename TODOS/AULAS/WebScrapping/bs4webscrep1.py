import requests
from bs4 import BeautifulSoup

url = "http://localhost:5500"
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, "html.parser")

Habilidade = parsed_html.select_one('#contato')
parent = Habilidade.parent
paragrafos = parent.select("p")

for p in parent.select("p"):
    print(p.text)
