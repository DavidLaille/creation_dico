from wiktionnaireparser import WiktionnaireParser as wiktp

url_base_wiki_online = 'https://fr.wiktionary.org/wiki/'
url_base_wiki_local_old = 'http://127.0.0.1:8080/wiktionary_fr_all_maxi_2022-07/A/'
url_base_wiki_local = 'http://127.0.0.1:8080/wiktionary_fr_all_nopic_2022-10/A/'

page = wiktp.from_source(url_base_wiki_local, 'martyre')

# print("html : ", page.html)
# print("PyQuery : ", page._query)
print("Sections : ", page.sections_id)

# etymology = page.get_etymology()
# print("étymologie : ", etymology)
data = page.get_word_data
print("Word data : ", page.get_word_data)
speech = page.get_parts_of_speech()
print("Parts of speech : ", speech)

if speech is not None:
    for i in range(len(speech.keys())):
        definitions = page.get_definitions(list(speech.keys())[i])
        print("defs : ", definitions)
        for j, definition in enumerate(definitions):
            print(j, definitions[j]['definition'])

# if speech['Nom commun']:
#     for index in range(len(speech['Nom commun'])):
#         print(f"definition n° {index} : {speech['Nom commun'][index]}")
#
# if speech['Verbe']:
#     for index in range(len(speech['Verbe'])):
#         print(f"definition n° {index} : {speech['Verbe'][index]}")
#
# if speech['Adjectif']:
#     for index in range(len(speech['Adjectif'])):
#         print(f"definition n° {index} : {speech['Adjectif'][index]}")
#
# if speech['Pronom interrogatif']:
#     for index in range(len(speech['Pronom interrogatif'])):
#         print(f"definition n° {index} : {speech['Nom commun'][index]}")
#
# if speech['Pronom relatif']:
#     for index in range(len(speech['Pronom relatif'])):
#         print(f"definition n° {index} : {speech['Pronom relatif'][index]}")
#
# if speech['Interjection']:
#     for index in range(len(speech['Interjection'])):
#         print(f"definition n° {index} : {speech['Interjection'][index]}")
#
# if speech['Adverbe interrogatif']:
#     for index in range(len(speech['Adverbe interrogatif'])):
#         print(f"definition n° {index} : {speech['Adverbe interrogatif'][index]}")


# # It is also possible to pick a word at random.
# page.random_page()
# print(page.get_title())

# # Use get_word_data to extract and display all data
# page = wiktp.from_source('anglophone')
# page.get_word_data
