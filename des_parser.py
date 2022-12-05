import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import re

# récupération du html avec une requête get
url_base_DES_online = 'https://crisco2.unicaen.fr/des/synonymes/'

mot = 'voix'
r = requests.get(url_base_DES_online + mot)
# print(r.text)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
# print(r.text)
# print(r.json())

# Parsing
only_synonymes = SoupStrainer(id="synonymes")
only_cliques = SoupStrainer(id="cliques")
only_li_tags = SoupStrainer("li")
# soup = BeautifulSoup(r.content, 'html.parser')
soup = BeautifulSoup(r.content, 'html.parser', parse_only=only_synonymes)
soup2 = BeautifulSoup(r.content, 'html.parser', parse_only=only_cliques)
# print(soup.prettify())
# print(soup.get_text())

regexp = re.compile(r'\xa0')
synonymes = []
for link in soup.find_all("a"):
    if "/des/synonymes/" in link.get("href"):
        word = link.get_text()
        # print(link.get_text())
        if '\xa0' in word:
            # print("Mot avant suppression : ", word)
            word = re.sub(regexp, "", word)
            # print("Mot après suppression : ", word)

        if word != mot and word not in synonymes:
            synonymes.append(word)

print("Synonymes : ", synonymes)
print("######################################")

cliques = []
for child in soup2.find_all("li"):
    # print(child.get_text())
    words = child.get_text()
    if '\n' in words:
        # print("Mots avant suppression 1 : ", words)
        words = words.replace('\n', "")
        # print("Mots après suppression 1 : ", words)
    if ' ' in words:
        # print("Mots avant suppression 2 : ", words)
        words = words.replace(' ', "")
        # print("Mots après suppression 2 : ", words)
    if mot in words:
        # print("Mots avant suppression 3 : ", words)
        words = words.replace(mot, "")
        # print("Mots après suppression 3 : ", words)
    # on enlève la dernière virgule
    words = words[:-1]
    cliques.append(words)

print("Cliques : ", cliques)

# regexp = re.compile('[^ \t\r\f\v]')
# ligne = ''
# lignes_syn = []
# for text in soup.get_text():
#     if text == '\n':
#         lignes_syn.append(ligne)
#         print(ligne)
#         # print("On change de ligne")
#         ligne = ''
#     else:
#         ligne += text
#
# print("############################")
# print("Lignes lues : ")
# print(lignes_syn)
#
# ligne = ''
# lignes_cliques = []
# for text in soup2.get_text():
#     if text == '\n':
#         lignes_cliques.append(ligne)
#         ligne = ''
#     else:
#         ligne += text
#
# print("############################")
# print("Lignes lues : ")
# print(lignes_cliques)

# for link in soup.find_all('a'):
#     print(link.get('href'))

