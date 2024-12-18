import csv
import json

# for working with local files
import glob
import os
from os.path import join

file_count = 0

for file in glob.glob('./collection-2/item_metadata/im_*.json'):
    file_count += 1
    print(file)

print('found',file_count)

list_of_item_metadata_files = list()
for file in glob.glob('./collection-2/item_metadata/im_*.json'):
    list_of_item_metadata_files.append(file)

print(len(list_of_item_metadata_files))

with open(list_of_item_metadata_files[0], 'r', encoding='utf-8') as item:
    print('file:',list_of_item_metadata_files[0],'\n')

    item_data = json.load(item)

#    for element in item_data.keys():
#        print(element,':',item_data[element])


collection_info_csv = 'collection_items_data.csv'


headers = ['source_file', 'item_id', 'title', 'creation_date', 'source_url', 'resource_type', 'language', 'rights_advisory', 'rights_info',
           'description', 'creators', 'loc_subjects', 'location']

# try first with one file
with open(list_of_item_metadata_files[0], 'r', encoding='utf-8') as data:
    # load the item data
    item_data = json.load(data)

    # extract the data you want
    # for checking purposes, add in the source of the info
    source_file = str(file)
    # make sure there's some unique and stable identifier
    try:
        item_id = item_data['item']['control_number']
    except:
        item_id = item_data['url'].split('/')[-2]
    title = item_data['title']
    date = item_data['created_published_date']
    source_url = item_data['url']
    try:
        creator = item_data['contributor_names']
    except:
        creator = 'Not found'
    try:
        description = item_data['summary']
    except:
        description = item_data['notes']
    try:
        resource_type = item_data['item']['format']
    except:
        resource_type = 'Not found'
    try:
        lang = item_data['item']['language']
    except:
        lang = 'Not found'
    try:
        location = item_data['item']['place'][0]['title']
    except:
        location = 'Not found'
    try:
        rights_ad = item_data['rights_advisory']
    except:
        rights_ad = 'Undetermined'
    try:
        rights_info = item_data['rights_information']
    except:
        rights_info = 'Undetermined'
    sub_head = item_data['subject_headings']


    # dictionary for the rows
    row_dict = dict()

    # look for the item metadata, assign it to the dictionary;
    # start with some basic elements likely (already enumerated in the headers list) :
    # source file
    row_dict['source_file'] = source_file
    # identifier
    row_dict['item_id'] = item_id
    # title
    row_dict['title'] = title
    # date
    row_dict['creation_date'] = date
    # link
    row_dict['source_url'] = source_url
    # format
    row_dict['resource_type'] = resource_type
    # language
    row_dict['language'] = lang
    #rights advisory
    row_dict['rights_advisory'] = rights_ad
    #rights info
    row_dict['rights_info'] = rights_info
    #description
    row_dict['description'] = description
    #creators
    row_dict['creators'] = creator
    #subjects
    row_dict['loc_subjects'] = sub_head
    #location
    row_dict['location'] = location
    print('created row dictionary:',row_dict)

    # write to the csv
#    with open(collection_info_csv, 'w', encoding='utf-8') as fout:
#        writer = csv.DictWriter(fout, fieldnames=headers)
#        writer.writeheader()
#        writer.writerow(row_dict)
#        print('wrote',collection_info_csv)
from datetime import date

date_string_for_today = date.today().strftime('%Y-%m-%d')

print(date_string_for_today)

collection_info_csv = os.path.join('.', 'collection_items_data2.csv')
file_count = 0
items_written = 0
error_count = 0

headers = ['item_type', 'date_uploaded', 'source_file', 'item_id', 'title', 'creation_date', 'source_url', 'resource_type', 'language', 'rights_advisory', 'rights_info',
           'description', 'creators', 'loc_subjects', 'location', 'image_url']

for file in list_of_item_metadata_files:
    file_count += 1
    print('opening',file)
    with open(file, 'r', encoding='utf-8') as item:
        # load the item data
        try:
            item_data = json.load(item)
        except:
            print('error loading',file)
            error_count += 1
            continue

        item_type = 'Item'
        # date uplaoded
        date_uploaded = date_string_for_today
        source_file = str(file)
        try:
            item_id = item_data['item']['control_number']
        except:
            item_id = item_data['url'].split('/')[-2]
        title = item_data['title']
        try:
            date = item_data['created_published_date']
        except:
            date = item_data['date']
        source_url = item_data['url']
        try:
            creator = item_data['contributor_names']
        except:
            creator = 'Not found'
        try:
            description = item_data['summary']
        except:
            description = item_data['notes']
        try:
            resource_type = item_data['item']['format'][0]
        except:
            resource_type = 'Not found'
        try:
            lang = item_data['item']['language'][0]
        except:
            lang = 'Not found'
        try:
            location = item_data['item']['place'][0]['title']
        except:
            location = 'Not found'
        try:
            rights_ad = item_data['rights_advisory']
        except:
            rights_ad = 'Undetermined'
        try:
            rights_info = item_data['rights_information']
        except:
            rights_info = 'Undetermined'
        try:
            sub_head = item_data['subject_headings']
        except:
            sub_head = 'No LOC subject heading found'
        try:
            image_url = item_data['image_url'][-1]
        except:
            image_url = 'Did not identify a URL'

        # dictionary for the rows
        row_dict = dict()

        row_dict['item_type'] = item_type
        # date uploaded
        row_dict['date_uploaded'] = date_uploaded
        # source file
        row_dict['source_file'] = source_file
        # identifier
        row_dict['item_id'] = item_id
        # title
        row_dict['title'] = title
        # date
        row_dict['creation_date'] = date
        # link
        row_dict['source_url'] = source_url
        # format
        row_dict['resource_type'] = resource_type
        # language
        row_dict['language'] = lang
        #rights advisory
        row_dict['rights_advisory'] = rights_ad
        #rights info
        row_dict['rights_info'] = rights_info
        #description
        row_dict['description'] = description
        #creators
        row_dict['creators'] = creator
        #subjects
        row_dict['loc_subjects'] = sub_head
        #location
        row_dict['location'] = location
        #image url
        row_dict['image_url'] = image_url

        #write to csv
        with open(collection_info_csv, 'a', encoding='utf-8', newline='') as fout:
            writer = csv.DictWriter(fout, fieldnames=headers)
            if items_written == 0:
                writer.writeheader()
            writer.writerow(row_dict)
            items_written += 1
            print('adding',item_id)

print('\n\n--- LOG ---')
print('wrote',collection_info_csv)
print('with',items_written,'items')
print(error_count,'errors (info not written)')