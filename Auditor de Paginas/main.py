import requests
from bs4 import BeautifulSoup
 
urls = 'https://ucsm.edu.pe/'
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

full_urls = []

for link in soup.find_all("a"):
   data = link.get('href')
   if data != "#" and data != "":
      if data.find("http") == -1:
        data = urls + data
      full_urls.append(data)

f = open("reporte.txt", "w")
for iterator in full_urls:
  try:
    x = requests.get(iterator)
    f.write(iterator)
    f.write(" : ")
    f.write(str(x.status_code))
    f.write("\n")
  except:
    f.write(iterator)
    f.write(" : 300 || No permite scrappers")
    f.write("\n")

f.close()