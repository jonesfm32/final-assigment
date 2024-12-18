import csv
import json
import requests
import os
from os.path import join

endpoint = 'https://www.loc.gov/free-to-use'
parameters = {
    'fo' : 'json'
}
collection = 'travel-posters'
collection_list_response = requests.get(endpoint + '/' + collection, params=parameters)
## print(collection_list_response.url)
collection_json = collection_list_response.json()

json_file = os.path.join('.','collection-2','collection-2-info.json')
with open(json_file, 'w', encoding='utf-8') as f:
    f.write(json.dumps(collection_json))
    print('wrote',f.name)

print(collection_json)
print(collection_json.keys())

for m in collection_json['content']['set']['items']:
    print(m)

print(len(collection_json['content']['set']['items']))
print(collection_json['content']['set']['items'][0].keys())

collection_list = './collection-2/collection_2_list.csv'
headers = ['image','link','title']

with open(collection_list, 'w', encoding='utf-8', newline= '') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for item in collection_json['content']['set']['items']:
        ## i was having issues with the strip function writing to the csv oddly
        writer.writerow(item)
    print('wrote',collection_list)