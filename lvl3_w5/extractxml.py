# Extracting Data from XML
#
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
#
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_169294.xml (Sum ends with 15)

# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

import urllib
import xml.etree.ElementTree as ET

# address = urllib.urlopen("http://python-data.dr-chuck.net/comments_42.xml").read()
address = raw_input('Enter location: ')
xml = urllib.urlopen(address).read()

print 'Retrieving', address
print 'Retrieved', len(xml), 'characters'

tree = ET.fromstring(xml)
counts = tree.findall('.//count')
# or comments = tree.findall('comments/comment')
print 'Count:', len(counts)

lst = []
for count in counts:
	lst.append(int(count.text))

print 'Sum:', sum(lst)
