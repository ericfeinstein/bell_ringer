import boto3
import json
from pprint import  pprint as pp
from sets import Set
import os
import logging
logging.basicConfig(filename='fruit/bell/example.log',level=logging.INFO,format='%(asctime)s %(message)s')

logging.info("Starting S3 Reader")
print "s3 Reader"

s3 = boto3.resource('s3')

try:
	file = open('fruit/bell/data.txt', 'r')
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
    print "S3 Opened"
    for key in bucket.objects.all():
        response = key.get()['Body'].read()
        for item in json.loads(response):
        	ring.add(item['account.id'])

print ring

## dont ring twice!
print "ring these" , list(ring - rang)

#os.system('python bell_ringer.py')
new_customers =  len(list(ring - rang))
print new_customers, "New Customers"

if new_customers > 0:
	os.system('python fruit/bell/bell_ringer.py')

## update the list

filen = open("fruit/bell/data.txt", "wb+")
filen.seek(0)
sep = ''
for ids in ring | rang:
	if ids!='' and ids!='\n':
		filen.write(sep)
		filen.write(ids)
		sep=","
