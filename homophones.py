import csv

import pandas as pd

LEXIQUE = 'data/Lexique383.tsv'
lex = pd.read_csv(LEXIQUE, sep='\t')
# print(lex.head())

print(f"Taille du lexique avant suppression des doublons : {len(lex)}")
lex_clean = lex.drop_duplicates(subset=['ortho'], keep='first', ignore_index=True)
print(f"Taille du lexique après suppression des doublons : {len(lex_clean)}")
print(lex_clean.head())

words = lex_clean['ortho'].tolist()
phon_words = lex_clean['phon'].tolist()
phon_renv_words = lex_clean['phonrenv'].tolist()
print(words[0:20])
# print(phon_words)
# print(phonrenv_words)

dico_homophones = dict()
dico_phon_renv = dict()
dico_contenu = dict()
dico_conteneur = dict()

dico_rimes_r1 = dict()
dico_rimes_r2 = dict()
dico_rimes_r3 = dict()
dico_rimes_r4 = dict()
dico_rimes_r5 = dict()
dico_rimes_r6 = dict()
dico_meme_debut_r1 = dict()
dico_meme_debut_r2 = dict()
dico_meme_debut_r3 = dict()
dico_meme_debut_r4 = dict()
dico_meme_debut_r5 = dict()
dico_meme_debut_r6 = dict()
dico_voisins_phonologiques_r1 = dict()
dico_voisins_phonologiques_r2 = dict()
dico_voisins_phonologiques_r3 = dict()


current_homophones = list()
current_phon_renv = list()
current_contenu = list()
current_conteneur = list()
current_rimes_r1 = list()
current_rimes_r2 = list()
current_rimes_r3 = list()
current_rimes_r4 = list()
current_rimes_r5 = list()
current_rimes_r6 = list()
current_meme_debut_r1 = list()
current_meme_debut_r2 = list()
current_meme_debut_r3 = list()
current_meme_debut_r4 = list()
current_meme_debut_r5 = list()
current_meme_debut_r6 = list()
current_voisins_phonologiques_r1 = list()
current_voisins_phonologiques_r2 = list()
current_voisins_phonologiques_r3 = list()

for i, word in enumerate(words):
    if i > 20:
        continue

    phon_ref = phon_words[i]
    print(f"{i} - Mot référence : {word} - Phonologie : {phon_ref}")

    current_homophones = []
    current_phon_renv = []
    current_contenu = []
    current_conteneur = []

    current_rimes_r1 = []
    current_rimes_r2 = []
    current_rimes_r3 = []
    current_rimes_r4 = []
    current_rimes_r5 = []
    current_rimes_r6 = []

    current_meme_debut_r1 = []
    current_meme_debut_r2 = []
    current_meme_debut_r3 = []
    current_meme_debut_r4 = []
    current_meme_debut_r5 = []
    current_meme_debut_r6 = []

    current_voisins_phonologiques_r1 = []
    current_voisins_phonologiques_r2 = []
    current_voisins_phonologiques_r3 = []

    for j, phon_word in enumerate(phon_words):
        if i != j:
            if phon_ref == phon_word:
                # print(f"Mot homophone : {words[j]} - Phonologie : {phon_words[j]}")
                current_homophones.append(words[j])
            if phon_ref[:-1] == phon_word or phon_ref == phon_word[:-1]:
                # print(f"Voisin phonologique de rang 1 : {words[j]} - Phonologie : {phon_words[j]}")
                current_voisins_phonologiques_r1.append(words[j])
            if len(phon_ref) == len(phon_word):
                counter = 0
                for num_son, son in enumerate(phon_ref):
                    if son != phon_word[num_son]:
                        counter += 1
                if counter == 1 and len(phon_ref) > 1:
                    # print(f"Voisin phonologique de rang 1 : {words[j]} - Phonologie : {phon_words[j]}")
                    current_voisins_phonologiques_r1.append(words[j])
                elif counter == 2 and len(phon_ref) > 2:
                    # print(f"Voisin phonologique de rang 2 : {words[j]} - Phonologie : {phon_words[j]}")
                    current_voisins_phonologiques_r2.append(words[j])
                elif counter == 3 and len(phon_ref) > 3:
                    # print(f"Voisin phonologique de rang 2 : {words[j]} - Phonologie : {phon_words[j]}")
                    current_voisins_phonologiques_r3.append(words[j])
            if phon_ref[-6:] == phon_word[-6:] and len(phon_ref) > 6:  # si les 6 derniers phonèmes sont identiques
                # print(f"6 derniers phonèmes du mot ref : {phon_ref[-6:]} - 6 derniers phonèmes du mot test : {phon_ref[-6:]}")
                # print(f"Mot qui rime de rang 6 : {words[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r6.append(words[j])
            elif phon_ref[-5:] == phon_word[-5:] and len(phon_ref) > 5:  # si les 5 derniers phonèmes sont identiques
                # print(f"5 derniers phonèmes du mot ref : {phon_ref[-5:]} - 5 derniers phonèmes du mot test : {phon_ref[-5:]}")
                # print(f"Mot qui rime de rang 5 : {words[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r5.append(words[j])
            elif phon_ref[-4:] == phon_word[-4:] and len(phon_ref) > 4:  # si les 4 derniers phonèmes sont identiques
                # print(f"4 derniers phonèmes du mot ref : {phon_ref[-4:]} - 4 derniers phonèmes du mot test : {phon_ref[-4:]}")
                # print(f"Mot qui rime de rang 4 : {words[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r4.append(words[j])
            elif phon_ref[-3:] == phon_word[-3:] and len(phon_ref) > 3:  # si les 3 derniers phonèmes sont identiques
                # print(f"3 derniers phonèmes du mot ref : {phon_ref[-3:]} - 3 derniers phonèmes du mot test : {phon_ref[-3:]}")
                # print(f"Mot qui rime de rang 3 : {words[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r3.append(words[j])
            elif phon_ref[-2:] == phon_word[-2:] and len(phon_ref) > 2:  # si les 2 derniers phonèmes sont identiques
                # print(f"2 derniers phonèmes du mot ref : {phon_ref[-2:]} - 2 derniers phonèmes du mot test : {phon_ref[-2:]}")
                # print(f"Mot qui rime de rang 2 : {words[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r2.append(words[j])
            elif phon_ref[-1:] == phon_word[-1:] and len(phon_ref) > 1:  # si le dernier phonème est identique (si ça rime)
                # print(f"Dernier phonème du mot ref : {phon_ref[-1:]} - Dernier phonème du mot test : {phon_ref[-1:]}")
                # print(f"Mot qui rime de rang 1 : {words[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r1.append(words[j])

            if phon_ref[:6] == phon_word[:6] and len(phon_ref) > 6:  # si les 6 premiers phonèmes sont identiques
                # print(f"6 premiers phonèmes du mot ref : {phon_ref[:6]} - 6 premiers phonèmes du mot test : {phon_ref[:6]}")
                # print(f"Mot qui commence pareil de rang 6 : {words[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r6.append(words[j])
            elif phon_ref[:5] == phon_word[:5] and len(phon_ref) > 5:  # si les 5 premiers phonèmes sont identiques
                # print(f"5 premiers phonèmes du mot ref : {phon_ref[:5]} - 5 premiers phonèmes du mot test : {phon_ref[:5]}")
                # print(f"Mot qui commence pareil de rang 5 : {words[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r5.append(words[j])
            elif phon_ref[:4] == phon_word[:4] and len(phon_ref) > 4:  # si les 4 derniers phonèmes sont identiques
                # print(f"4 premiers phonèmes du mot ref : {phon_ref[:4]} - 4 premiers phonèmes du mot test : {phon_ref[:4]}")
                # print(f"Mot qui commence pareil de rang 4 : {words[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r4.append(words[j])
            elif phon_ref[:3] == phon_word[:3] and len(phon_ref) > 3:  # si les 3 derniers phonèmes sont identiques
                # print(f"3 premiers phonèmes du mot ref : {phon_ref[:3]} - 3 premiers phonèmes du mot test : {phon_ref[:3]}")
                # print(f"Mot qui commence pareil de rang 3 : {words[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r3.append(words[j])
            elif phon_ref[:2] == phon_word[:2] and len(phon_ref) > 2:  # si les 2 derniers phonèmes sont identiques
                # print(f"2 premiers phonèmes du mot ref : {phon_ref[:2]} - 2 premiers phonèmes du mot test : {phon_ref[:2]}")
                # print(f"Mot qui commence pareil de rang 2 : {words[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r2.append(words[j])
            elif phon_ref[:1] == phon_word[:1] and len(phon_ref) > 1:  # si le dernier phonème est identique (si ça rime)
                # print(f"Premier phonème du mot ref : {phon_ref[:1]} - Premier phonème du mot test : {phon_ref[:1]}")
                # print(f"Mot qui commence pareil de rang 1 : {words[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r1.append(words[j])

            if len(phon_ref) > 1 and len(phon_word) > 1:
                if len(phon_word) < len(phon_ref) and phon_word in phon_ref:
                    current_contenu.append(words[j])
                elif len(phon_ref) < len(phon_word) and phon_ref in phon_word:
                    current_conteneur.append(words[j])

        if phon_ref == phon_renv_words[j]:
            # print(f"Mot avec phonologie renversée : {words[j]} - Phonologie : {phon_words[j]}")
            current_phon_renv.append(words[j])

    if current_homophones:
        dico_homophones[word] = current_homophones
    if current_phon_renv:
        dico_phon_renv[word] = current_phon_renv
    if current_contenu:
        dico_contenu[word] = current_contenu
    if current_conteneur:
        dico_conteneur[word] = current_conteneur

    if current_rimes_r6:
        dico_rimes_r6[word] = current_rimes_r6
    if current_rimes_r5:
        dico_rimes_r5[word] = current_rimes_r5
    if current_rimes_r4:
        dico_rimes_r4[word] = current_rimes_r4
    if current_rimes_r3:
        dico_rimes_r3[word] = current_rimes_r3
    if current_rimes_r2:
        dico_rimes_r2[word] = current_rimes_r2
    if current_rimes_r1:
        dico_rimes_r1[word] = current_rimes_r1

    if current_meme_debut_r6:
        dico_meme_debut_r6[word] = current_meme_debut_r6
    if current_meme_debut_r5:
        dico_meme_debut_r5[word] = current_meme_debut_r5
    if current_meme_debut_r4:
        dico_meme_debut_r4[word] = current_meme_debut_r4
    if current_meme_debut_r3:
        dico_meme_debut_r3[word] = current_meme_debut_r3
    if current_meme_debut_r2:
        dico_meme_debut_r2[word] = current_meme_debut_r2
    if current_meme_debut_r1:
        dico_meme_debut_r1[word] = current_meme_debut_r1

    if current_voisins_phonologiques_r1:
        dico_voisins_phonologiques_r1[word] = current_voisins_phonologiques_r1
    if current_voisins_phonologiques_r2:
        dico_voisins_phonologiques_r2[word] = current_voisins_phonologiques_r2
    if current_voisins_phonologiques_r3:
        dico_voisins_phonologiques_r3[word] = current_voisins_phonologiques_r3

########################################################################################################################
# # Affichage des listes de mots trouvées
# # Affichage des homophones
# print("###############################################################################################################")
# for key, value in dico_homophones.items():
#     print(f"Mot : {key}")
#     print(f"Homophones : {dico_homophones[key]}")
#
# # Affichage des mots qui se prononcent pareil à l'envers (phonologie renversée identique)
# print("###############################################################################################################")
# for key, value in dico_phon_renv.items():
#     print(f"Mot : {key}")
#     print(f"Mots à phonologie renversée identique : {dico_phon_renv[key]}")
#
# # Affichage des mots qui sont contenus dans le mot actuel
# print("###############################################################################################################")
# for key, value in dico_contenu.items():
#     print(f"Mot : {key}")
#     print(f"Mots à phonologie renversée identique : {dico_contenu[key]}")
#
# # Affichage des mots qui contiennent dans le mot actuel
# print("###############################################################################################################")
# for key, value in dico_conteneur.items():
#     print(f"Mot : {key}")
#     print(f"Mots à phonologie renversée identique : {dico_conteneur[key]}")
#
# # Affichage des rimes de rang 6 (6 derniers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_rimes_r6.items():
#     print(f"Mot : {key}")
#     print(f"Rimes de rang 6 : {dico_rimes_r6[key]}")
#
# # Affichage des rimes de rang 5 (5 derniers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_rimes_r5.items():
#     print(f"Mot : {key}")
#     print(f"Rimes de rang 5 : {dico_rimes_r5[key]}")
#
# # Affichage des rimes de rang 4 (4 derniers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_rimes_r4.items():
#     print(f"Mot : {key}")
#     print(f"Rimes de rang 4 : {dico_rimes_r4[key]}")
#
# # Affichage des rimes de rang 3 (3 derniers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_rimes_r3.items():
#     print(f"Mot : {key}")
#     print(f"Rimes de rang 3 : {dico_rimes_r3[key]}")
#
# # Affichage des rimes de rang 2 (2 derniers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_rimes_r2.items():
#     print(f"Mot : {key}")
#     print(f"Rimes de rang 2 : {dico_rimes_r2[key]}")
#
# # # Affichage des rimes de rang 1 (juste le dernier phonème identique)
# # print("###############################################################################################################")
# # for key, value in dico_rimes_r1.items():
# #     print(f"Mot : {key}")
# #     print(f"Rimes de rang 1 : {dico_rimes_r1[key]}")
#
#
# # Affichage des mots commençant pareil de rang 6 (6 premiers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_meme_debut_r6.items():
#     print(f"Mot : {key}")
#     print(f"Mots commençant pareil de rang 6 : {dico_meme_debut_r6[key]}")
#
# # Affichage des mots commençant pareil de rang 5 (5 premiers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_meme_debut_r5.items():
#     print(f"Mot : {key}")
#     print(f"Mots commençant pareil de rang 5 : {dico_meme_debut_r5[key]}")
#
# # Affichage des mots commençant pareil de rang 4 (4 premiers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_meme_debut_r4.items():
#     print(f"Mot : {key}")
#     print(f"Mots commençant pareil de rang 4 : {dico_meme_debut_r4[key]}")
#
# # Affichage des mots commençant pareil de rang 3 (3 premiers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_meme_debut_r3.items():
#     print(f"Mot : {key}")
#     print(f"Mots commençant pareil de rang 3 : {dico_meme_debut_r3[key]}")
#
# # Affichage des mots commençant pareil de rang 2 (2 premiers phonèmes identiques)
# print("###############################################################################################################")
# for key, value in dico_meme_debut_r2.items():
#     print(f"Mot : {key}")
#     print(f"Mots commençant pareil de rang 2 : {dico_meme_debut_r2[key]}")
#
# # # Affichage des mots commençant pareil de rang 1 (juste le premier phonème identique)
# # print("###############################################################################################################")
# # for key, value in dico_meme_debut_r1.items():
# #     print(f"Mot : {key}")
# #     print(f"Mots commençant pareil de rang 1 : {dico_meme_debut_r1[key]}")
#
# # Affichage des voisins phonologiques de rang 1 (un seul phonème différent)
# print("###############################################################################################################")
# for key, value in dico_voisins_phonologiques_r1.items():
#     print(f"Mot : {key}")
#     print(f"Voisins phonologiques de rang 1 : {dico_voisins_phonologiques_r1[key]}")
#
# # Affichage des voisins phonologiques de rang 2 (2 phonèmes différents)
# print("###############################################################################################################")
# for key, value in dico_voisins_phonologiques_r2.items():
#     print(f"Mot : {key}")
#     print(f"Voisins phonologiques de rang 2 : {dico_voisins_phonologiques_r2[key]}")
#
# # # Affichage des voisins phonologiques de rang 3 (3 phonèmes différents)
# # print("###############################################################################################################")
# # for key, value in dico_voisins_phonologiques_r3.items():
# #     print(f"Mot : {key}")
# #     print(f"Voisins phonologiques de rang 3 : {dico_voisins_phonologiques_r3[key]}")
########################################################################################################################

########################################################################################################################
# Sauvegarde des listes de mots trouvées
# Sauvegarde des homophones
print("###############################################################################################################")
with open("data/homophones.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 21):  # on crée 20 colonnes
        header.append("h_" + str(i))
    writer.writerow(header)
    for key, value in dico_homophones.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des homophones sauvegardé.")

# Sauvegarde des mots qui se prononcent pareil à l'envers (phonologie renversée identique)
print("###############################################################################################################")
with open("data/homophones_reverse.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 21):  # on crée 20 colonnes
        header.append("hr_" + str(i))
    writer.writerow(header)
    for key, value in dico_phon_renv.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des homophones renversés sauvegardé.")

# Sauvegarde des mots contenus dans un autre mot
print("###############################################################################################################")
with open("data/contenus.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 501):  # on crée 500 colonnes
        header.append("in_" + str(i))
    writer.writerow(header)
    for key, value in dico_contenu.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots contenus sauvegardé.")

# Sauvegarde des mots contenants un autre mot
print("###############################################################################################################")
with open("data/contenants.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 201):  # on crée 200 colonnes
        header.append("around_" + str(i))
    writer.writerow(header)
    for key, value in dico_conteneur.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots contenants sauvegardé.")

# Sauvegarde des rimes de rang 6 (6 derniers phonèmes identiques)
print("###############################################################################################################")
with open("data/rimes_r6.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 21):  # on crée 20 colonnes
        header.append("r6_" + str(i))
    writer.writerow(header)
    for key, value in dico_rimes_r6.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des rimes de rang 6 sauvegardé.")

# Sauvegarde des rimes de rang 5 (5 derniers phonèmes identiques)
print("###############################################################################################################")
with open("data/rimes_r5.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 21):  # on crée 50 colonnes
        header.append("r5_" + str(i))
    writer.writerow(header)
    for key, value in dico_rimes_r5.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des rimes de rang 5 sauvegardé.")

# Sauvegarde des rimes de rang 4 (4 derniers phonèmes identiques)
print("###############################################################################################################")
with open("data/rimes_r4.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 101):  # on crée 100 colonnes
        header.append("r4_" + str(i))
    writer.writerow(header)
    for key, value in dico_rimes_r4.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des rimes de rang 4 sauvegardé.")

# Sauvegarde des rimes de rang 3 (3 derniers phonèmes identiques)
print("###############################################################################################################")
with open("data/rimes_r3.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 501):  # on crée 500 colonnes
        header.append("r3_" + str(i))
    writer.writerow(header)
    for key, value in dico_rimes_r3.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des rimes de rang 3 sauvegardé.")

# Sauvegarde des rimes de rang 2 (2 derniers phonèmes identiques)
print("###############################################################################################################")
with open("data/rimes_r2.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 2001):  # on crée 2000 colonnes
        header.append("r2_" + str(i))
    writer.writerow(header)
    for key, value in dico_rimes_r2.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des rimes de rang 2 sauvegardé.")

# Sauvegarde des rimes de rang 1 (juste le dernier phonème identique)
print("###############################################################################################################")
with open("data/rimes_r1.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 15001):  # on crée 15000 colonnes
        header.append("r1_" + str(i))
    writer.writerow(header)
    for key, value in dico_rimes_r1.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des rimes de rang 1 sauvegardé.")


# Sauvegarde des mots commençant pareil de rang 6 (6 premiers phonèmes identiques)
print("###############################################################################################################")
with open("data/meme_debut_r6.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 21):  # on crée 20 colonnes
        header.append("md_r6_" + str(i))
    writer.writerow(header)
    for key, value in dico_meme_debut_r6.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots commençant pareil de rang 6 sauvegardé.")

# Sauvegarde des mots commençant pareil de rang 5 (5 premiers phonèmes identiques)
print("###############################################################################################################")
with open("data/meme_debut_r5.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 21):  # on crée 50 colonnes
        header.append("md_r5_" + str(i))
    writer.writerow(header)
    for key, value in dico_meme_debut_r5.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots commençant pareil de rang 5 sauvegardé.")

# Sauvegarde des mots commençant pareil de rang 4 (4 premiers phonèmes identiques)
print("###############################################################################################################")
with open("data/meme_debut_r4.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 101):  # on crée 100 colonnes
        header.append("md_r4_" + str(i))
    writer.writerow(header)
    for key, value in dico_meme_debut_r4.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots commençant pareil de rang 4 sauvegardé.")

# Sauvegarde des mots commençant pareil de rang 3 (3 premiers phonèmes identiques)
print("###############################################################################################################")
with open("data/meme_debut_r3.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 501):  # on crée 500 colonnes
        header.append("md_r3_" + str(i))
    writer.writerow(header)
    for key, value in dico_meme_debut_r3.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots commençant pareil de rang 3 sauvegardé.")

# Sauvegarde des mots commençant pareil de rang 2 (2 premiers phonèmes identiques)
print("###############################################################################################################")
with open("data/meme_debut_r2.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 2001):  # on crée 2000 colonnes
        header.append("md_r2_" + str(i))
    writer.writerow(header)
    for key, value in dico_meme_debut_r2.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots commençant pareil de rang 2 sauvegardé.")

# Sauvegarde des mots commençant pareil de rang 1 (juste le premier phonème identique)
print("###############################################################################################################")
with open("data/meme_debut_r1.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 15001):  # on crée 15000 colonnes
        header.append("md_r1_" + str(i))
    writer.writerow(header)
    for key, value in dico_meme_debut_r1.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des mots commençant pareil de rang 1 sauvegardé.")

# Sauvegarde des voisins phonologiques de rang 1 (un seul phonème différent)
print("###############################################################################################################")
with open("data/voisins_phonologiques_r1.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 201):  # on crée 200 colonnes
        header.append("vp_r1_" + str(i))
    writer.writerow(header)
    for key, value in dico_voisins_phonologiques_r1.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des voisins phonologiques de rang 1 sauvegardé.")

# Sauvegarde des voisins phonologiques de rang 2 (2 phonèmes différents)
print("###############################################################################################################")
with open("data/voisins_phonologiques_r2.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 201):  # on crée 200 colonnes
        header.append("vp_r2_" + str(i))
    writer.writerow(header)
    for key, value in dico_voisins_phonologiques_r2.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des voisins phonologiques de rang 2 sauvegardé.")

# Sauvegarde des voisins phonologiques de rang 3 (3 phonèmes différents)
print("###############################################################################################################")
with open("data/voisins_phonologiques_r3.csv", 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)

    header = ["Mot"]
    for i in range(1, 5001):  # on crée 5000 colonnes
        header.append("vp_r3_" + str(i))
    writer.writerow(header)
    for key, value in dico_voisins_phonologiques_r3.items():
        row = value
        row.insert(0, key)
        # print("Ligne à ajouter : ", row)
        writer.writerow(row)

print("Fichier des voisins phonologiques de rang 3 sauvegardé.")
