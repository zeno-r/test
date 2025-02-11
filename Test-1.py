"""
    Test_1 -- Simple entity identification
    Author:  Roberta Zeno (rz3192@nyu.edu)
    Last Revised:  2/11/2025
"""

import spacy
nlp = spacy.load('en_core_web_sm')
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import textwrap

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 '
                         'Safari/537.36'}

response = requests.get('https://www.cnbc.com/2025/02/11/musks-97point4-billion-for-openai-aims-to-slow-down-a-competitor-sam-altman-says.html', headers = headers)

soup = BeautifulSoup(response.text, 'html.parser')
article = []

paragraphs = [p.get_text() for p in soup.find_all('p')]
for para in paragraphs:
    if len(para) > 100:
        article.append(para)

for i in article[:-1]:
    my_article = textwrap.fill(i, width = 165, replace_whitespace = True)
    print()
    print(my_article)

print('==============================================================================================')

doc = nlp(my_article)
for entity in doc.ents:
    print(f'Entity name & type: {entity.text, entity.label_}')
