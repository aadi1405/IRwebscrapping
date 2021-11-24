import os
import sys

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["ir"]
collection = database["webdata"]

print("Select one of the keywords:")
print(['Computer Vision', 'Deep Learning',
      'Face Mask Detection', 'Haar Cascade Algorithm', 'K nearest neighbor'])
keyword = input("Enter Keyword: ")

query = {"keyword": keyword}
try:
    document = list(collection.find(query))[0]
except IndexError:
    print("Keyword not found")
    sys.exit()

print("Files Found: ")
print(list(document['files'].keys()))

filename = input('Enter Filename: ')
try:
    os.startfile(document['files'][filename])
except KeyError:
    print("File not found")
    sys.exit()
