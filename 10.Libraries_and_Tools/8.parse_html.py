from bs4 import BeautifulSoup
import requests

def parse_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

url = "http://example.com"
print("HTML da phan tich cua trang web la:", parse_html(url))
