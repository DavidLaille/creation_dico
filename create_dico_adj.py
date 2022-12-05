from wiktionnaireparser import WiktionnaireParser as wiktp
import csv
import pandas as pd


url_base_wiki_online = 'https://fr.wiktionary.org/wiki/'
url_base_wiki_local = 'http://127.0.0.1:8080/wiktionary_fr_all_maxi_2022-07/A/'
url_base_wiki_local = 'http://127.0.0.1:8080/wiktionary_fr_all_nopic_2022-10/A/'

adj_path = 'data/lemmes_adj2.csv'
adj = pd.read_csv(adj_path, sep=',')

# Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(adj.head())

adj_not_found = []
num_def = 1

##############################################################################
# Récupération des définitions
##############################################################################
for a in adj.lemme:
    # print("Adjectif : ", a)
    # if a == 'vrai':  # cette condition sert pour tester/éviter de parcourir tous les adjectifs
    #     break
    num_def = 1
    page = wiktp.from_source(url_base_wiki_local, a)
    if page == "error":
        adj_not_found.append(a)
        print(f"The word {a} has not been found on the wiktionnaire")
        continue
    else:
        speech = page.get_parts_of_speech()
        # print("Parts of speech : ", speech)
        if speech is not None:
            for i in range(len(speech.keys())):
                definitions = page.get_definitions(list(speech.keys())[i])
                for j, definition in enumerate(definitions):
                    # print(f"definition n° {i+1} : {definitions[i]['definition']}")
                    col_word = f"def_{num_def}"  # i+1 : juste pour démarrer à partir de 1
                    adj.loc[adj.lemme == a, col_word] = definitions[j]['definition']
                    num_def += 1

print("#########################################################################")

# Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(adj.head())

##############################################################################
# Écriture des dataframes dans un fichier csv
##############################################################################
adj.to_csv("data/lemmes_adj_avec_def.csv")
print("fichier csv enregistré")

##############################################################################
# Écriture des mots non trouvés dans des fichiers csv
##############################################################################
with open("data/adj_not_found.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['adj_not_found'])
    for a in adj_not_found:
        writer.writerow([a])
print("fichier des adj non trouvés enregistré")
