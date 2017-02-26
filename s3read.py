import boto3
import json
from pprint import  pprint as pp
from sets import Set
import os

s3 = boto3.resource('s3')

try:
	file = open('data.txt', 'r')
	txt = file.read()
	arr = txt.split(',')
	rang = Set(arr)
	file.close()
except:
	print "no data"
	rang = Set([])
# bucket = s3.bucket('ringthebell')

ring = Set([])

for bucket in s3.buckets.all():
    for key in bucket.objects.all():
        response = key.get()['Body'].read()
        for item in json.loads(response):
        	ring.add(item['account.id'])


## dont ring twice!
print "ring these" , list(ring - rang)

#os.system('python bell_ringer.py')
new_customers =  len(list(ring - rang))
print new_customers, "New Customers"

if new_customers > 0:
	os.system('python bell_ringer.py')

## update the list

filen = open("data.txt", "wb+")
filen.seek(0)
sep = ''
for ids in ring | rang:
	if ids!='' and ids!='\n':
		filen.write(sep)
		filen.write(ids)
		sep=","

