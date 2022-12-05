from wiktionaryparser import WiktionaryParser

parser = WiktionaryParser()
word = parser.fetch('test')
another_word = parser.fetch('test', 'french')

parser.set_default_language('french')
parser.exclude_part_of_speech('verb')
parser.include_relation('alternative forms')
a_third_word = parser.fetch('amour')
print("Mot 1 :", word)
print("Mot 2 :", another_word)
print("Mot 3 :", a_third_word)

