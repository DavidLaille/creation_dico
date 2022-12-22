import csv
import pandas as pd

LEXIQUE = 'data/Lexique383.tsv'
lex = pd.read_csv(LEXIQUE, sep='\t')

print(f"Taille du lexique avant suppression des doublons : {len(lex)}")
lex_only_lemmes = lex.drop_duplicates(subset=['lemme'], keep='first', ignore_index=True)
print(f"Taille du lexique après suppression des doublons : {len(lex_only_lemmes)}")
# print(lex_only_lemmes.head())

lex_only_lemmes = lex_only_lemmes[['ortho', 'phon', 'lemme', 'cgram', 'genre', 'nombre', 'freqlemfilms2', 'freqlemlivres']]
# print(lex_only_lemmes.head())

########################################################################################################################
# Si on veut trier par fréquence d'apparition décroissante
# Fréquence d'apparition dans les sous-titres de film
lex_only_lemmes = lex_only_lemmes.sort_values(by=['freqlemfilms2'], ascending=False, ignore_index=True)
# Fréquence d'apparition dans les livres
# lex_only_lemmes = lex_only_lemmes.sort_values(by=['freqlemfilms2'], ascending=False, ignore_index=True)

print(lex_only_lemmes.head())


lex_only_lemmes.to_csv("data/dico_lemmes.csv", sep=',', header=True,  encoding='utf8')
print("Fichiers 'dico_lemmes.csv' sauvegardé avec succès.")



