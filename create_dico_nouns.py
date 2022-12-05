from wiktionnaireparser import WiktionnaireParser as wiktp
import csv
import pandas as pd


url_base_wiki_online = 'https://fr.wiktionary.org/wiki/'
url_base_wiki_local_old = 'http://127.0.0.1:8080/wiktionary_fr_all_maxi_2022-07/A/'
url_base_wiki_local = 'http://127.0.0.1:8080/wiktionary_fr_all_nopic_2022-10/A/'

nouns_path = 'data/lemmes_noms2.csv'
nouns = pd.read_csv(nouns_path, sep=',')

# Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(names.head())

nouns_not_found = []
num_def = 1

##############################################################################
# Récupération des définitions
##############################################################################
for noun in nouns.lemme:
    # print("Nom : ", noun)
    # if noun == 'temps':  # cette condition sert pour tester/éviter de parcourir tous les noms
    #     break
    num_def = 1
    page = wiktp.from_source(url_base_wiki_local, noun)
    if page == "error":
        nouns_not_found.append(noun)
        print(f"The word {noun} has not been found on the wiktionnaire")
        continue
    else:
        speech = page.get_parts_of_speech()
        # print("Parts of speech : ", speech)
        if speech is not None:
            for i in range(len(speech.keys())):
                definitions = page.get_definitions(list(speech.keys())[i])
                for j, definition in enumerate(definitions):
                    # print(f"definition n° {i+1} : {definitions[i]['definition']}")
                    col_word = f"def_{num_def}"
                    nouns.loc[nouns.lemme == noun, col_word] = definitions[j]['definition']
                    num_def += 1

print("#########################################################################")

##############################################################################
# Écriture des dataframes dans un fichier csv
##############################################################################
nouns.to_csv("data/lemmes_noms_avec_def.csv")
print("fichier csv enregistré")

##############################################################################
# Écriture des mots non trouvés dans des fichiers csv
##############################################################################
with open("data/nouns_not_found.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['nouns_not_found'])
    for n in nouns_not_found:
        writer.writerow([n])
print("fichier des noms non trouvés enregistré")
