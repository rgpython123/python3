from bs4 import BeautifulSoup
import httplib2

http = httplib2.Http()
status, response = http.request('http://www.pythonforbeginners.com')

soup = BeautifulSoup(response)

for link in soup.find_all('a', href=True):
    print link['href']
