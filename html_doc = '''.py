from bs4 import BeautifulSoup
import requests as req

commit_messages = []

with open(r"S:\Everything\commit_messages.txt", 'a', encoding='utf-8') as fl:
    for _ in range(200):
        a = req.get("https://whatthecommit.com").content
        soup = BeautifulSoup(a, 'html.parser')
        print(soup.p.string, file=fl, end='')
