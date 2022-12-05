import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import pandas as pd
import csv
import time


nouns_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_noms2.csv'
nouns = pd.read_csv(nouns_path, sep=',')

# récupération du html avec une requête get
url_base_DES_online = 'https://crisco2.unicaen.fr/des/synonymes/'

# Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(nouns.head())

count = 0
nouns_not_found = []
num_def = 1
# Parsing
only_synonymes = SoupStrainer(id="synonymes")
only_cliques = SoupStrainer(id="cliques")

##############################################################################
# Récupération des synonymes
##############################################################################
for noun in nouns.lemme:
    # if noun == nouns.lemme[5]:  # cette condition sert à ne tester que les premiers noms
    #     break
    print("Nom : ", noun)

    # si on veut tester un seul mot
    # if noun != 'temps':
    #     continue

    r = requests.get(url_base_DES_online + noun)

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

                if word != noun and word not in synonymes:
                    synonymes.append(word)

        # print("Synonymes : ", synonymes)
        # print("Synonymes ordonnés : ", synonymes_ord)
        # print("######################################")
        for j, synonyme in enumerate(synonymes_ord):
            col_word = f"syn_{num_syn}"
            nouns.loc[nouns.lemme == noun, col_word] = synonymes_ord[j]
            num_syn += 1

    else:
        nouns_not_found.append(noun)
        print(f"The word {noun} has not been found in the DES")
        continue

    # on sauvegarde les données récoltées tous les 200 mots
    if count > 200:
        print("################# Sauvegarde intermédiaire #################")
        count = 0
        nouns.to_csv("data/lemmes_noms_avec_syn.csv")

    # si besoin de ralentir le nombre de requêtes
    # time.sleep(0.5)
    count += 1

print("#########################################################################")

##############################################################################
# Écriture des dataframes dans un fichier csv
##############################################################################
nouns.to_csv("data/lemmes_noms_avec_syn.csv")
print("fichier csv enregistré")

##############################################################################
# Écriture des mots non trouvés dans des fichiers csv
##############################################################################
with open("data/nouns_not_found_syn.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['nouns_not_found'])
    for n in nouns_not_found:
        writer.writerow([n])
print("fichier des noms non trouvés enregistré")