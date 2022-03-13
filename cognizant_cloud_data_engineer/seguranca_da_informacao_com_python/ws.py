from bs4 import BeautifulSoup
import requests

#recebe requisicao do site
site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/968/cascavel-ce").content

#Objeto soup baixa o site em html
soup = BeautifulSoup(site, 'html.parser')

#Transforma html em string e imprime
#print(soup.prettify())
print(soup)

temp_min = soup.find("span", id="min-temp-1")
temp_max = soup.find("span", id="max-temp-1")

print(f'Temperatura em Cascavel-Ce\n  Max: {temp_max.string}\n  Min: {temp_min.string}')
