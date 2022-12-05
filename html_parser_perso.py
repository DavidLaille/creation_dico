import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# récupération du html avec une requête get
url_base_wiki_online = 'https://fr.wiktionary.org/wiki/'
url_base_wiki_local = 'http://127.0.0.1:8080/wiktionary_fr_all_nopic_2022-10/A/'

r = requests.get(url_base_wiki_online + "voler")
# print(html_response.text)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
# print(r.text)
# print(r.json())

# Parsing
only_li_tags = SoupStrainer("li")
soup = BeautifulSoup(r.content, 'html.parser', parse_only=only_li_tags)
# print(soup.prettify())
# print(soup.get_text())


# print("####################################################################")
# print(soup.prettify())
# print("avant : ", soup.get_text())
# print("####################################################################")
# print(soup.find_all("ul"))
for line in soup.find_all('ul'):
    # print("##################")
    # print("line : ", line)
    line.decompose()
    # print(line.get_text())
    # print("##################")

count = 10
for phrase in soup.find_all('li'):
    if count <= 0:
        break
    print("##################")
    print("phrase n° ", count, " : ", phrase.get_text())
    print("##################")
    count -= 1

# print("####################################################################")
# print(soup.prettify())
# print("après : ", soup.get_text())
# print("####################################################################")
