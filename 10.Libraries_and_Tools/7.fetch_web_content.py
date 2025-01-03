import requests

def fetch_web_content(url):
    response = requests.get(url)
    return response.text

url = "http://example.com"
print("Noi dung trang web la:", fetch_web_content(url))
