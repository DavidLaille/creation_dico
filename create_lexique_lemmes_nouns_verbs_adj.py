import csv
import pandas as pd

LEXIQUE = 'data/Lexique383.tsv'
lex = pd.read_csv(LEXIQUE, sep='\t')
# lex.to_csv('data/lexique383.csv', sep=',', header=True,  encoding='utf8')

print(f"Taille du lexique avant suppression des doublons : {len(lex)}")
# lex_only_lemmes = lex.drop_duplicates(subset=['lemme'], keep='first', ignore_index=True)
lex_only_lemmes = lex.loc[lex.lemme == lex.ortho]
print(f"Taille du lexique après suppression des doublons : {len(lex_only_lemmes)}")
# print(lex_only_lemmes.head())

lex_only_lemmes = lex_only_lemmes[['lemme', 'phon', 'cgram', 'nblettres', 'freqlemfilms2', 'freqlemlivres']]
# lex_only_lemmes = lex_only_lemmes.reindex(columns=['lemme', 'phon', 'cgram', 'freqlemfilms2', 'freqlemlivres'])
# print(lex_only_lemmes.head())

########################################################################################################################
# Si on veut trier par fréquence d'apparition décroissante
# Fréquence d'apparition dans les sous-titres de film
lex_only_lemmes = lex_only_lemmes.sort_values(by=['freqlemfilms2'], ascending=False, ignore_index=True)
# Fréquence d'apparition dans les livres
# lex_only_lemmes = lex_only_lemmes.sort_values(by=['freqlemfilms2'], ascending=False, ignore_index=True)

print(lex_only_lemmes.head())

lex_only_lemmes.to_csv("data/lexique_lemmes.csv", sep=',', header=True,  encoding='utf8')
print("Fichiers 'dico_lemmes.csv' sauvegardé avec succès.")

########################################################################################################################
# Si on ne veut garder que certaines catégories grammaticales (ici les noms, verbes et adjectifs)
nouns = lex_only_lemmes.loc[lex_only_lemmes.cgram == 'NOM']
verbs = lex_only_lemmes.loc[lex_only_lemmes.cgram == 'VER']
adjs = lex_only_lemmes.loc[lex_only_lemmes.cgram == 'ADJ']
print(nouns)
print(verbs)
print(adjs)

nouns_verbs_adjs = lex_only_lemmes.loc[(lex_only_lemmes.cgram == 'NOM') |
                                       (lex_only_lemmes.cgram == 'VER') |
                                       (lex_only_lemmes.cgram == 'ADJ')]
print(nouns_verbs_adjs)

nouns.to_csv("data/lexique_noms.csv", sep=',', header=True,  encoding='utf8')
print("Fichiers 'lexique_noms.csv' sauvegardé avec succès.")
verbs.to_csv("data/lexique_verbes.csv", sep=',', header=True,  encoding='utf8')
print("Fichiers 'lexique_verbes.csv' sauvegardé avec succès.")
adjs.to_csv("data/lexique_adjs.csv", sep=',', header=True,  encoding='utf8')
print("Fichiers 'lexique_adjs.csv' sauvegardé avec succès.")

nouns_verbs_adjs.to_csv("data/lexique_nouns_verbs_adjs.csv", sep=',', header=True,  encoding='utf8')
print("Fichiers 'lexique_nouns_verbs_adjs.csv' sauvegardé avec succès.")

nouns_verbs_adjs_mots_plus_de_3_lettres = nouns_verbs_adjs.loc[nouns_verbs_adjs.nblettres > 2]
nouns_verbs_adjs_mots_plus_de_3_lettres.to_csv("data/lexique_nouns_verbs_adjs_3+.csv",
                                               sep=',', header=True,  encoding='utf8')
print("Fichiers 'lexique_nouns_verbs_adjs_3+.csv' sauvegardé avec succès.")
