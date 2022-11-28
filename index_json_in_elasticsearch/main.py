import requests, json, os
from elasticsearch import Elasticsearch


directory = '/home/pierangelo/lavori/personali/python_samples/index_json_in_elasticsearch/'

res = requests.get('http://192.168.56.1:9200')
print (res.content)
es = Elasticsearch([{'host': '192.168.56.1', 'port': '9200'}])

'''
i = 1

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        f = open(filename)
        docket_content = f.read()
        # Send the data into es
        es.index(index='myindex', ignore=400, doc_type='docket', 
        id=i, body=json.loads(docket_content))
        i = i + 1
'''

id = 1
with open('dpc-covid19-ita-regioni.json') as json_data:
    data = json.load(json_data)
    for dat in data:
        print(json.dumps(dat))
        es.index(index='testdata', doc_type='generated', id=id, body=json.dumps(dat))
        id += 1


def ciao():
    
            
