# Extracting Data from JSON
#
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
#
# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_169298.json (Sum ends with 45)
#
# Sample Execution
#
# $ python solution.py
# Enter location: http://python-data.dr-chuck.net/comments_42.json
# Retrieving http://python-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2482

import urllib
import json

# url = urllib.urlopen("http://python-data.dr-chuck.net/comments_42.json").read()
url = raw_input('Enter location: ')
parsed_url = urllib.urlopen(url).read()
js = json.loads(parsed_url)

print 'Retrieving', url
print 'Retrieved', len(parsed_url), 'characters'

counts = []
for string in js['comments']:
	counts.append(string['count'])

print 'Count:', len(counts)
print 'Sum:', sum(counts)
