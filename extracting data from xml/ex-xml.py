import ssl
import urllib.request
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_621791.xml'

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('comments/comment/count')
sum = 0
count = 0
for r in results:
    count += 1
    sum += int(r.text)

print('Count:', count)
print('Sum:', sum)
