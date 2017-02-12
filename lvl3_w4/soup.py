###

import urllib
from BeautifulSoup import *

# enterUrl = raw_input('Enter URL: ')
parseHtml = urllib.urlopen('https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html').read()
soup = BeautifulSoup(parseHtml)

# Retrive all numbers
tags = soup('span')

count = 0
for tag in tags:
    parsedNumb = tag.contents[0]
    count += int(parsedNumb)

print(count)
