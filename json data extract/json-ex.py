import json
import ssl
import urllib.request

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_621792.json'

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
results = json.loads(data)

sum = 0
counter = 0
for r in results['comments']:
    counter += 1
    sum += int(r['count'])

print('Count:', counter)
print('Sum:', sum)
