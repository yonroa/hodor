#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level0.php"

res = requests.get(url)
print(res)
