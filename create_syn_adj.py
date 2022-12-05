import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import pandas as pd
import csv
import time


adj_path = 'data/lemmes_adj2.csv'
adjs = pd.read_csv(adj_path, sep=',')

# récupération du html avec une requête get
url_base_DES_online = 'https://crisco2.unicaen.fr/des/synonymes/'

# Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(nouns.head())

count = 0
adjs_not_found = []
num_def = 1
# Parsing
only_synonymes = SoupStrainer(id="synonymes")
only_cliques = SoupStrainer(id="cliques")

##############################################################################
# Récupération des synonymes
##############################################################################
for adj in adjs.lemme:
    # if noun == nouns.lemme[5]:  # cette condition sert à ne tester que les premiers noms
    #     break
    print("Adj : ", adj)

    # si on veut tester un seul mot
    # if noun != 'temps':
    #     continue

    r = requests.get(url_base_DES_online + adj)

    num_syn = 1
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser', parse_only=only_synonymes)
        soup2 = BeautifulSoup(r.content, 'html.parser', parse_only=only_cliques)

        synonymes = []
        synonymes_ord = []
        for link in soup.find_all("a"):
            if "/des/synonymes/" in link.get("href"):
                word = link.get_text()
                # print(link.get_text())
                if '\xa0' in word:
                    word = word.replace('\xa0', "")
                    synonymes_ord.append(word)
                    continue

                if word != adj and word not in synonymes:
                    synonymes.append(word)

        # print("Synonymes : ", synonymes)
        # print("Synonymes ordonnés : ", synonymes_ord)
        # print("######################################")
        for j, synonyme in enumerate(synonymes_ord):
            col_word = f"syn_{num_syn}"
            adjs.loc[adjs.lemme == adj, col_word] = synonymes_ord[j]
            num_syn += 1

    else:
        adjs_not_found.append(adj)
        print(f"The word {adj} has not been found in the DES")
        continue

    # on sauvegarde les données récoltées tous les 200 mots
    if count > 200:
        print("################# Sauvegarde intermédiaire #################")
        count = 0
        adjs.to_csv("data/lemmes_adjs_avec_syn.csv")

    # si besoin de ralentir le nombre de requêtes
    # time.sleep(0.5)
    count += 1

print("#########################################################################")

##############################################################################
# Écriture des dataframes dans un fichier csv
##############################################################################
adjs.to_csv("data/lemmes_adjs_avec_syn.csv")
print("fichier csv enregistré")

##############################################################################
# Écriture des mots non trouvés dans des fichiers csv
##############################################################################
with open("data/adjs_not_found_syn.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['adjs_not_found'])
    for n in adjs_not_found:
        writer.writerow([n])
print("fichier des adjectifs non trouvés enregistré")
