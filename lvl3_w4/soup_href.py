#

import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
html = urllib.urlopen('https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html').read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
