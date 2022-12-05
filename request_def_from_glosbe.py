import urllib  # library for fetching internet resources
import urllib.request
import json  # library for json operations

# import os
# title=os.environ["word"]
title = input("Enter word to search: ")  # Input word to search dictionary
print("Word: ", title)

# stores the json formatted output to a variable
url = 'https://glosbe.com/gapi_v0_1/translate?from=eng&dest=eng&format=json&phrase=' + title + '&pretty=true'

# json representation of url is stored in variable result
result = json.load(urllib.request.urlopen(url))

# get the first text in "meaning" in "tuc" from result
print("Meaning: ", result["tuc"][0]["meanings"][0]["text"])