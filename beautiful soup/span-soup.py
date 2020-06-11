import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup
sum = 0
count = 0

# ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve the span tags
tags = soup('span')
for tag in tags:
    t = int(tag.contents[0])
    sum += t
    count += 1

print('Count', count)
print('Sum', sum)
