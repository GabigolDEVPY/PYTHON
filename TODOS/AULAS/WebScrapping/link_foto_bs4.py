from bs4 import BeautifulSoup
import requests

url = "https://www.magazineluiza.com.br/webcam-logitech-c922-pro-hd-stream-ful-hd-com-tripe/p/ke126e5g42/in/webc/?ads=patrocinado&seller_id=inpower4"
response = requests.get(url)
content = response.text
parsed_html = BeautifulSoup(content, "html.parser")
print(parsed_html)
imgs = parsed_html.find_all("img")
print(imgs)
# links = [img["alt"] for img in imgs ]
# print(links)