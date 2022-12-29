import csv
import pandas as pd

LEXIQUE = 'data/Lexique383.tsv'
lex = pd.read_csv(LEXIQUE, sep='\t')
# print(lex.head())

print(f"Taille du lexique avant suppression des doublons : {len(lex)}")
lex_clean = lex.drop_duplicates(subset=['ortho'], keep='first', ignore_index=True)
print(f"Taille du lexique après suppression des doublons : {len(lex_clean)}")
print(lex_clean.head())

lex_lemmes = lex_clean[lex_clean['ortho'] == lex_clean['lemme']]
print(lex_lemmes.head())

words = lex_clean['ortho'].tolist()
lemmes = lex_lemmes['lemme'].tolist()
print(f"Premiers mots du lexique : {words[0:20]}")
print(f"Premiers mots du lexique des lemmes : {lemmes[0:20]}")
print(f"Taille du lexique : {len(words)}")
print(f"Taille du lexique des lemmes : {len(lemmes)}")

phon_words = lex_lemmes['phon'].tolist()
phon_renv_words = lex_lemmes['phonrenv'].tolist()
print(f"Liste des phonologies des mots : {phon_words[0:20]}")
print(f"Liste des phonologies inversées des mots : {phon_renv_words[0:20]}")
print(f"Taille de la liste des phonologies des mots : {len(phon_words)}")
print(f"Taille de la liste des phonologies inversées des mots : {len(phon_renv_words)}")

dico_homophones = dict()
dico_phon_renv = dict()
dico_contenu = dict()
dico_conteneur = dict()

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

########################################################################################################################
# Ouverture des fichiers csv (et création s'ils n'existent pas)
f_homophones = open("data/lexiques_homophonies_lemmes/homophones.csv", 'w', newline='', encoding='utf8')
writer_homophones = csv.writer(f_homophones)

f_homophones_reverse = open("data/lexiques_homophonies_lemmes/homophones_reverse.csv", 'w', newline='', encoding='utf8')
writer_homophones_reverse = csv.writer(f_homophones_reverse)

f_contenus = open("data/lexiques_homophonies_lemmes/contenus.csv", 'w', newline='', encoding='utf8')
writer_contenus = csv.writer(f_contenus)

f_contenants = open("data/lexiques_homophonies_lemmes/contenants.csv", 'w', newline='', encoding='utf8')
writer_contenants = csv.writer(f_contenants)

f_rimes_r6 = open("data/lexiques_homophonies_lemmes/rimes_r6.csv", 'w', newline='', encoding='utf8')
writer_rimes_r6 = csv.writer(f_rimes_r6)

f_rimes_r5 = open("data/lexiques_homophonies_lemmes/rimes_r5.csv", 'w', newline='', encoding='utf8')
writer_rimes_r5 = csv.writer(f_rimes_r5)

f_rimes_r4 = open("data/lexiques_homophonies_lemmes/rimes_r4.csv", 'w', newline='', encoding='utf8')
writer_rimes_r4 = csv.writer(f_rimes_r4)

f_rimes_r3 = open("data/lexiques_homophonies_lemmes/rimes_r3.csv", 'w', newline='', encoding='utf8')
writer_rimes_r3 = csv.writer(f_rimes_r3)

f_rimes_r2 = open("data/lexiques_homophonies_lemmes/rimes_r2.csv", 'w', newline='', encoding='utf8')
writer_rimes_r2 = csv.writer(f_rimes_r2)

f_meme_debut_r6 = open("data/lexiques_homophonies_lemmes/meme_debut_r6.csv", 'w', newline='', encoding='utf8')
writer_meme_debut_r6 = csv.writer(f_meme_debut_r6)

f_meme_debut_r5 = open("data/lexiques_homophonies_lemmes/meme_debut_r5.csv", 'w', newline='', encoding='utf8')
writer_meme_debut_r5 = csv.writer(f_meme_debut_r5)

f_meme_debut_r4 = open("data/lexiques_homophonies_lemmes/meme_debut_r4.csv", 'w', newline='', encoding='utf8')
writer_meme_debut_r4 = csv.writer(f_meme_debut_r4)

f_meme_debut_r3 = open("data/lexiques_homophonies_lemmes/meme_debut_r3.csv", 'w', newline='', encoding='utf8')
writer_meme_debut_r3 = csv.writer(f_meme_debut_r3)

f_meme_debut_r2 = open("data/lexiques_homophonies_lemmes/meme_debut_r2.csv", 'w', newline='', encoding='utf8')
writer_meme_debut_r2 = csv.writer(f_meme_debut_r2)

f_meme_debut_r1 = open("data/lexiques_homophonies_lemmes/meme_debut_r1.csv", 'w', newline='', encoding='utf8')
writer_meme_debut_r1 = csv.writer(f_meme_debut_r1)

f_voisins_phonologiques_r1 = open("data/lexiques_homophonies_lemmes/voisins_phonologiques_r1.csv",
                                  'w', newline='', encoding='utf8')
writer_voisins_phonologiques_r1 = csv.writer(f_voisins_phonologiques_r1)

f_voisins_phonologiques_r2 = open("data/lexiques_homophonies_lemmes/voisins_phonologiques_r2.csv",
                                  'w', newline='', encoding='utf8')
writer_voisins_phonologiques_r2 = csv.writer(f_voisins_phonologiques_r2)

f_voisins_phonologiques_r3 = open("data/lexiques_homophonies_lemmes/voisins_phonologiques_r3.csv",
                                  'w', newline='', encoding='utf8')
writer_voisins_phonologiques_r3 = csv.writer(f_voisins_phonologiques_r3)
########################################################################################################################

########################################################################################################################
# Création des en-tête pour chaque liste de mots
# En-tête des homophones
print("###############################################################################################################")
print("Début Création headers.")
header = ["Mot"]
for i in range(1, 21):  # on crée 20 colonnes
    header.append("h_" + str(i))
writer_homophones.writerow(header)

# En-tête des mots qui se prononcent pareil à l'envers (phonologie renversée identique)
header = ["Mot"]
for i in range(1, 21):  # on crée 20 colonnes
    header.append("hr_" + str(i))
writer_homophones_reverse.writerow(header)

# En-tête des mots contenus dans un autre mot
header = ["Mot"]
for i in range(1, 501):  # on crée 500 colonnes
    header.append("in_" + str(i))
writer_contenus.writerow(header)

# En-tête des mots contenants un autre mot
header = ["Mot"]
for i in range(1, 201):  # on crée 200 colonnes
    header.append("around_" + str(i))
writer_contenants.writerow(header)

# En-tête des rimes de rang 6 (6 derniers phonèmes identiques)
header = ["Mot"]
for i in range(1, 21):  # on crée 20 colonnes
    header.append("r6_" + str(i))
writer_rimes_r6.writerow(header)

# En-tête des rimes de rang 5 (5 derniers phonèmes identiques)
header = ["Mot"]
for i in range(1, 21):  # on crée 50 colonnes
    header.append("r5_" + str(i))
writer_rimes_r5.writerow(header)

# En-tête des rimes de rang 4 (4 derniers phonèmes identiques)
header = ["Mot"]
for i in range(1, 101):  # on crée 100 colonnes
    header.append("r4_" + str(i))
writer_rimes_r4.writerow(header)

# En-tête des rimes de rang 3 (3 derniers phonèmes identiques)
header = ["Mot"]
for i in range(1, 501):  # on crée 500 colonnes
    header.append("r3_" + str(i))
writer_rimes_r3.writerow(header)

# En-tête des rimes de rang 2 (2 derniers phonèmes identiques)
header = ["Mot"]
for i in range(1, 2001):  # on crée 2000 colonnes
    header.append("r2_" + str(i))
writer_rimes_r2.writerow(header)

# En-tête des mots commençant pareil de rang 6 (6 premiers phonèmes identiques)
header = ["Mot"]
for i in range(1, 51):  # on crée 20 colonnes
    header.append("md_r6_" + str(i))
writer_meme_debut_r6.writerow(header)

# En-tête des mots commençant pareil de rang 5 (5 premiers phonèmes identiques)
header = ["Mot"]
for i in range(1, 51):  # on crée 50 colonnes
    header.append("md_r5_" + str(i))
writer_meme_debut_r5.writerow(header)

# En-tête des mots commençant pareil de rang 4 (4 premiers phonèmes identiques)
header = ["Mot"]
for i in range(1, 201):  # on crée 100 colonnes
    header.append("md_r4_" + str(i))
writer_meme_debut_r4.writerow(header)

# En-tête des mots commençant pareil de rang 3 (3 premiers phonèmes identiques)
header = ["Mot"]
for i in range(1, 1501):  # on crée 500 colonnes
    header.append("md_r3_" + str(i))
writer_meme_debut_r3.writerow(header)

# En-tête des mots commençant pareil de rang 2 (2 premiers phonèmes identiques)
header = ["Mot"]
for i in range(1, 2001):  # on crée 2000 colonnes
    header.append("md_r2_" + str(i))
writer_meme_debut_r2.writerow(header)

# En-tête des mots commençant pareil de rang 1 (juste le premier phonème identique)
header = ["Mot"]
for i in range(1, 15001):  # on crée 15000 colonnes
    header.append("md_r1_" + str(i))
writer_meme_debut_r1.writerow(header)

# En-tête des voisins phonologiques de rang 1 (un seul phonème différent)
header = ["Mot"]
for i in range(1, 201):  # on crée 200 colonnes
    header.append("vp_r1_" + str(i))
writer_voisins_phonologiques_r1.writerow(header)

# En-tête des voisins phonologiques de rang 2 (2 phonèmes différents)
header = ["Mot"]
for i in range(1, 201):  # on crée 200 colonnes
    header.append("vp_r2_" + str(i))
writer_voisins_phonologiques_r2.writerow(header)

# En-tête des voisins phonologiques de rang 3 (3 phonèmes différents)
header = ["Mot"]
for i in range(1, 5001):  # on crée 5000 colonnes
    header.append("vp_r3_" + str(i))
writer_voisins_phonologiques_r3.writerow(header)
print("Fin Création headers.")
print("###############################################################################################################")

for i, word in enumerate(lemmes):
    # if i > 20:
    #     continue

    phon_ref = phon_words[i]
    print(f"{i} - Mot référence : {word} - Phonologie : {phon_ref}")

    current_homophones = []
    current_phon_renv = []
    current_contenu = []
    current_conteneur = []

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
                # print(f"Mot homophone : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_homophones.append(lemmes[j])
            if phon_ref[:-1] == phon_word or phon_ref == phon_word[:-1]:
                # print(f"Voisin phonologique de rang 1 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_voisins_phonologiques_r1.append(lemmes[j])
            if len(phon_ref) == len(phon_word):
                counter = 0
                for num_son, son in enumerate(phon_ref):
                    if son != phon_word[num_son]:
                        counter += 1
                if counter == 1 and len(phon_ref) > 1:
                    # print(f"Voisin phonologique de rang 1 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                    current_voisins_phonologiques_r1.append(lemmes[j])
                elif counter == 2 and len(phon_ref) > 2:
                    # print(f"Voisin phonologique de rang 2 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                    current_voisins_phonologiques_r2.append(lemmes[j])
                elif counter == 3 and len(phon_ref) > 3:
                    # print(f"Voisin phonologique de rang 2 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                    current_voisins_phonologiques_r3.append(lemmes[j])
            if phon_ref[-6:] == phon_word[-6:] and len(phon_ref) > 6:  # si les 6 derniers phonèmes sont identiques
                # print(f"6 derniers phonèmes du mot ref : {phon_ref[-6:]} - 6 derniers phonèmes du mot test : {phon_ref[-6:]}")
                # print(f"Mot qui rime de rang 6 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r6.append(lemmes[j])
            elif phon_ref[-5:] == phon_word[-5:] and len(phon_ref) > 5:  # si les 5 derniers phonèmes sont identiques
                # print(f"5 derniers phonèmes du mot ref : {phon_ref[-5:]} - 5 derniers phonèmes du mot test : {phon_ref[-5:]}")
                # print(f"Mot qui rime de rang 5 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r5.append(lemmes[j])
            elif phon_ref[-4:] == phon_word[-4:] and len(phon_ref) > 4:  # si les 4 derniers phonèmes sont identiques
                # print(f"4 derniers phonèmes du mot ref : {phon_ref[-4:]} - 4 derniers phonèmes du mot test : {phon_ref[-4:]}")
                # print(f"Mot qui rime de rang 4 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r4.append(lemmes[j])
            elif phon_ref[-3:] == phon_word[-3:] and len(phon_ref) > 3:  # si les 3 derniers phonèmes sont identiques
                # print(f"3 derniers phonèmes du mot ref : {phon_ref[-3:]} - 3 derniers phonèmes du mot test : {phon_ref[-3:]}")
                # print(f"Mot qui rime de rang 3 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r3.append(lemmes[j])
            elif phon_ref[-2:] == phon_word[-2:] and len(phon_ref) > 2:  # si les 2 derniers phonèmes sont identiques
                # print(f"2 derniers phonèmes du mot ref : {phon_ref[-2:]} - 2 derniers phonèmes du mot test : {phon_ref[-2:]}")
                # print(f"Mot qui rime de rang 2 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_rimes_r2.append(lemmes[j])

            if phon_ref[:6] == phon_word[:6] and len(phon_ref) > 6:  # si les 6 premiers phonèmes sont identiques
                # print(f"6 premiers phonèmes du mot ref : {phon_ref[:6]} - 6 premiers phonèmes du mot test : {phon_ref[:6]}")
                # print(f"Mot qui commence pareil de rang 6 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r6.append(lemmes[j])
            elif phon_ref[:5] == phon_word[:5] and len(phon_ref) > 5:  # si les 5 premiers phonèmes sont identiques
                # print(f"5 premiers phonèmes du mot ref : {phon_ref[:5]} - 5 premiers phonèmes du mot test : {phon_ref[:5]}")
                # print(f"Mot qui commence pareil de rang 5 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r5.append(lemmes[j])
            elif phon_ref[:4] == phon_word[:4] and len(phon_ref) > 4:  # si les 4 derniers phonèmes sont identiques
                # print(f"4 premiers phonèmes du mot ref : {phon_ref[:4]} - 4 premiers phonèmes du mot test : {phon_ref[:4]}")
                # print(f"Mot qui commence pareil de rang 4 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r4.append(lemmes[j])
            elif phon_ref[:3] == phon_word[:3] and len(phon_ref) > 3:  # si les 3 derniers phonèmes sont identiques
                # print(f"3 premiers phonèmes du mot ref : {phon_ref[:3]} - 3 premiers phonèmes du mot test : {phon_ref[:3]}")
                # print(f"Mot qui commence pareil de rang 3 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r3.append(lemmes[j])
            elif phon_ref[:2] == phon_word[:2] and len(phon_ref) > 2:  # si les 2 derniers phonèmes sont identiques
                # print(f"2 premiers phonèmes du mot ref : {phon_ref[:2]} - 2 premiers phonèmes du mot test : {phon_ref[:2]}")
                # print(f"Mot qui commence pareil de rang 2 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r2.append(lemmes[j])
            elif phon_ref[:1] == phon_word[:1] and len(phon_ref) > 1:  # si le dernier phonème est identique (si ça rime)
                # print(f"Premier phonème du mot ref : {phon_ref[:1]} - Premier phonème du mot test : {phon_ref[:1]}")
                # print(f"Mot qui commence pareil de rang 1 : {lemmes[j]} - Phonologie : {phon_words[j]}")
                current_meme_debut_r1.append(lemmes[j])

            if len(phon_ref) > 1 and len(phon_word) > 1:
                if len(phon_word) < len(phon_ref) and phon_word in phon_ref:
                    current_contenu.append(lemmes[j])
                elif len(phon_ref) < len(phon_word) and phon_ref in phon_word:
                    current_conteneur.append(lemmes[j])

        if phon_ref == phon_renv_words[j]:
            # print(f"Mot avec phonologie renversée : {lemmes[j]} - Phonologie : {phon_words[j]}")
            current_phon_renv.append(lemmes[j])

    if current_homophones:
        row = current_homophones
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_homophones.writerow(row)
    if current_phon_renv:
        row = current_phon_renv
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_homophones_reverse.writerow(row)
    if current_contenu:
        row = current_contenu
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_contenus.writerow(row)
    if current_conteneur:
        row = current_conteneur
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_contenants.writerow(row)

    if current_rimes_r6:
        row = current_rimes_r6
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_rimes_r6.writerow(row)
    if current_rimes_r5:
        row = current_rimes_r5
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_rimes_r5.writerow(row)
    if current_rimes_r4:
        row = current_rimes_r4
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_rimes_r4.writerow(row)
    if current_rimes_r3:
        row = current_rimes_r3
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_rimes_r3.writerow(row)
    if current_rimes_r2:
        row = current_rimes_r2
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_rimes_r2.writerow(row)

    if current_meme_debut_r6:
        row = current_meme_debut_r6
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_meme_debut_r6.writerow(row)
    if current_meme_debut_r5:
        row = current_meme_debut_r5
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_meme_debut_r5.writerow(row)
    if current_meme_debut_r4:
        row = current_meme_debut_r4
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_meme_debut_r4.writerow(row)
    if current_meme_debut_r3:
        row = current_meme_debut_r3
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_meme_debut_r3.writerow(row)
    if current_meme_debut_r2:
        row = current_meme_debut_r2
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_meme_debut_r2.writerow(row)
    if current_meme_debut_r1:
        row = current_meme_debut_r1
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_meme_debut_r1.writerow(row)

    if current_voisins_phonologiques_r1:
        row = current_voisins_phonologiques_r1
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_voisins_phonologiques_r1.writerow(row)
    if current_voisins_phonologiques_r2:
        row = current_voisins_phonologiques_r2
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_voisins_phonologiques_r2.writerow(row)
    if current_voisins_phonologiques_r3:
        row = current_voisins_phonologiques_r3
        row.insert(0, word)
        # print("Ligne à ajouter : ", row)
        writer_voisins_phonologiques_r3.writerow(row)

f_homophones.close()
f_homophones_reverse.close()
f_contenus.close()
f_contenants.close()
f_rimes_r6.close()
f_rimes_r5.close()
f_rimes_r4.close()
f_rimes_r3.close()
f_rimes_r2.close()
f_meme_debut_r6.close()
f_meme_debut_r5.close()
f_meme_debut_r4.close()
f_meme_debut_r3.close()
f_meme_debut_r2.close()
f_meme_debut_r1.close()
f_voisins_phonologiques_r1.close()
f_voisins_phonologiques_r2.close()
f_voisins_phonologiques_r3.close()
