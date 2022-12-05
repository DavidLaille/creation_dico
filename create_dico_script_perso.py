import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

names_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_noms2.csv'
verbs_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_verbes2.csv'
adj_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_adj2.csv'

names = pd.read_csv(names_path, sep=',')
verbs = pd.read_csv(verbs_path, sep=',')
adj = pd.read_csv(adj_path, sep=',')

# on crée une nouvelle colonne dans chaque dataframe
names = names.assign(definition='def')
verbs = verbs.assign(definition='def')
adj = adj.assign(definition='def')

print(names.head())
print(verbs.head())
print(adj.head())

##############################################################################
# Récupération des définitions
##############################################################################
url_base = "http://192.168.16.230:8080/wiktionary_fr_all_maxi_2022-07/A/"
# on définit un SoupStrainer pour ne prendre dans le HTML que les balises <li></li>
only_li_tags = SoupStrainer("li")
# nombre de définitions qu'on souhaite récupérer
nb_def = 1

for name in names.lemme:
    # print("Nom: ", name)
    # on crée l'url avec le mot actuel
    url = url_base + name
    # print(url)
    # on récupère le résultat de la requête en json
    response = requests.get(url)
    if response.status_code == 200:
        # on parse la réponse html reçue
        soup = BeautifulSoup(response.content, 'html.parser', parse_only=only_li_tags)
        # on supprime les sous-listes (parties entre les balises <ul></ul>)
        for line in soup.find_all('ul'):
            line.decompose()
        # on va chercher la première balise <li></li>
        # cette première balise contient la première définition du mot
        # si la structure des HTML fournis par le Wiktionnaire change,
        # il faudra modifier la recherche des définitions
        count = 1
        for phrase in soup.find_all('li'):
            if count <= 0:
                break
            # print("##################")
            # print("phrase n° ", count, " : ", phrase.get_text())
            # print("##################")
            count -= 1
            # on met la définition obtenue dans la colonne definition du dataframe
            names.loc[names.lemme == name, 'definition'] = phrase.get_text()

for verb in verbs.lemme:
    # print("Verbe: ", verb)
    # on crée l'url avec le mot actuel
    url = url_base + verb
    # print(url)
    # on récupère le résultat de la requête en json
    response = requests.get(url)
    if response.status_code == 200:
        # on parse la réponse html reçue
        soup = BeautifulSoup(response.content, 'html.parser', parse_only=only_li_tags)
        # on supprime les sous-listes (parties entre les balises <ul></ul>)
        for line in soup.find_all('ul'):
            line.decompose()
        # on va chercher la première balise <li></li>
        # cette première balise contient la première définition du mot
        # si la structure des HTML fournis par le Wiktionnaire change,
        # il faudra modifier la recherche des définitions
        count = 1
        for phrase in soup.find_all('li'):
            if count <= 0:
                break
            # print("##################")
            # print("phrase n° ", count, " : ", phrase.get_text())
            # print("##################")
            count -= 1
            # on met la définition obtenue dans la colonne definition du dataframe
            verbs.loc[verbs.lemme == verb, 'definition'] = phrase.get_text()

for a in adj.lemme:
    # print("Verbe: ", verb)
    # on crée l'url avec le mot actuel
    url = url_base + a
    # print(url)
    # on récupère le résultat de la requête en json
    response = requests.get(url)
    if response.status_code == 200:
        # on parse la réponse html reçue
        soup = BeautifulSoup(response.content, 'html.parser', parse_only=only_li_tags)
        # on supprime les sous-listes (parties entre les balises <ul></ul>)
        for line in soup.find_all('ul'):
            line.decompose()
        # on va chercher la première balise <li></li>
        # cette première balise contient la première définition du mot
        # si la structure des HTML fournis par le Wiktionnaire change,
        # il faudra modifier la recherche des définitions
        count = 1
        for phrase in soup.find_all('li'):
            if count <= 0:
                break
            # print("##################")
            # print("phrase n° ", count, " : ", phrase.get_text())
            # print("##################")
            count -= 1
            # on met la définition obtenue dans la colonne definition du dataframe
            adj.loc[adj.lemme == a, 'definition'] = phrase.get_text()

# on écrit les dataframes modifiés dans un fichier csv
# names.to_csv("data/lemmes_noms_avec_def.csv")
# verbs.to_csv("data/lemmes_verbes_avec_def.csv")
# adj.to_csv("data/lemmes_adj_avec_def.csv")
