import json
import csv
import requests
from datetime import datetime

session = requests.Session()

paramsPost = {"":"","Accept: application/json, text/javascript, */*; q":"0.01"}
response = session.get("https://c2intel.com/data.php", data=paramsPost)
resp = response.json()
date = datetime.today().strftime('%Y-%m-%d')
with open('./IoCs_'+date+".csv", mode='a+') as csv_file:
    fieldnames = ['Host', 'Description', 'Source']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for each in resp:
        writer.writerow({'Host': each['host'],'Description': each['description'],'Source': each['source']})
