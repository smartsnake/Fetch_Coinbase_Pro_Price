import cbpro
from pymongo import MongoClient
from datetime import datetime
import time
from os import path
import os
import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)

public_client = cbpro.PublicClient()
client = MongoClient(os.environ['MONGODB_HOST'],
            27017)

db = client[data['database']]
collection = db[data['collection']]

while(not path.exists(data['end_file'])):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    Doc = public_client.get_product_24hr_stats(data['currency'])
    Doc.update({'timestamp' : timestamp})
    print(Doc)
    collection.insert_one(Doc)
    time.sleep(60)