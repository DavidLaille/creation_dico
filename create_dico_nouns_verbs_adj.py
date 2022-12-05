from wiktionnaireparser import WiktionnaireParser as wiktp
import csv
import pandas as pd

nouns_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_noms2.csv'
verbs_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_verbes2.csv'
adj_path = 'C:/dev/PycharmProjects/creation_dico/data/lemmes_adj2.csv'

nouns = pd.read_csv(nouns_path, sep=',')
verbs = pd.read_csv(verbs_path, sep=',')
adj = pd.read_csv(adj_path, sep=',')

# Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(names.head())
# print(verbs.head())
# print(adj.head())

nouns_not_found = []
verbs_not_found = []
adj_not_found = []
# nb_mots_def = 0

##############################################################################
# Récupération des définitions
##############################################################################
for noun in nouns.lemme:
    # print("Nom : ", noun)
    # if noun == 'temps':  # cette condition sert pour tester/éviter de parcourir tous les noms
    #     break
    page = wiktp.from_source(noun)
    if page == "error":
        nouns_not_found.append(noun)
        print(f"The word {noun} has not been found on the wiktionnaire")
        continue
    else:
        speech = page.get_parts_of_speech()
        # print("Parts of speech : ", speech)
        if speech is not None:
            # nb_mots_def += 1
            # print(nb_mots_def)
            definitions = page.get_definitions(list(speech.keys())[0])
            for i, definition in enumerate(definitions):
                # print(f"definition n° {i+1} : {definitions[i]['definition']}")
                col_word = "def_" + str(i+1)  # i+1 : juste pour démarrer à partir de 1
                nouns.loc[nouns.lemme == noun, col_word] = definitions[i]['definition']

print("#########################################################################")

for verb in verbs.lemme:
    print("Verbe : ", verb)
    # if verb == 'pouvoir':  # cette condition sert pour tester/éviter de parcourir tous les verbes
    #     break
    page = wiktp.from_source(verb)
    if page == "error":
        verbs_not_found.append(verb)
        print(f"The word {verb} has not been found on the wiktionnaire")
        continue
    else:
        speech = page.get_parts_of_speech()
        # print("Parts of speech : ", speech)
        if speech is not None:
            definitions = page.get_definitions(list(speech.keys())[0])
            for i, definition in enumerate(definitions):
                # print(f"definition n° {i+1} : {definitions[i]['definition']}")
                col_word = "def_" + str(i+1)
                verbs.loc[verbs.lemme == verb, col_word] = definitions[i]['definition']

print("#########################################################################")

for a in adj.lemme:
    print("Adjectif : ", a)
    # if a == 'vrai':  # cette condition sert pour tester/éviter de parcourir tous les adjectifs
    #     break
    page = wiktp.from_source(a)
    if page == "error":
        adj_not_found.append(a)
        print(f"The word {a} has not been found on the wiktionnaire")
        continue
    else:
        speech = page.get_parts_of_speech()
        # print("Parts of speech : ", speech)
        if speech is not None:
            definitions = page.get_definitions(list(speech.keys())[0])
            for i, definition in enumerate(definitions):
                # print(f"definition n° {i+1} : {definitions[i]['definition']}")
                col_word = "def_" + str(i+1)
                adj.loc[adj.lemme == a, col_word] = definitions[i]['definition']

print("#########################################################################")

# # Quelques prints pour vérifier si le chargement des données s'est bien passé
# print(nouns.head())
# print(verbs.head())
# print(adj.head())
#
##############################################################################
# Écriture des dataframes dans un fichier csv
##############################################################################
nouns.to_csv("data/lemmes_noms_avec_def.csv")
verbs.to_csv("data/lemmes_verbes_avec_def.csv")
adj.to_csv("data/lemmes_adj_avec_def.csv")
print("fichiers csv enregistrés")

##############################################################################
# Écriture des mots non trouvés dans des fichiers csv
##############################################################################
with open("data/nouns_not_found.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['nouns_not_found'])
    for n in nouns_not_found:
        writer.writerow([n])
print("fichier des noms non trouvés enregistré")

with open("data/verbs_not_found.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['verbs_not_found'])
    for v in verbs_not_found:
        writer.writerow([v])
print("fichier des verbes non trouvés enregistré")

with open("data/adj_not_found.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['adj_not_found'])
    for a in adj_not_found:
        writer.writerow([a])
print("fichier des adj non trouvés enregistré")
