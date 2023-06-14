import requests
from bs4 import BeautifulSoup

rus_word = "говорить"
conj_url = f"https://cooljugator.com/ru/{rus_word}"

r = requests.get(conj_url)
if r.status_code == 200:
    resp_text = r.text
    soup = BeautifulSoup(resp_text, features="html.parser")
    print(soup.findAll("div", class_="ui label blue")[0].contents)
