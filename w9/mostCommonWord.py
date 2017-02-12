# Set dictionary, and find out most common word in the file

	# Opening and reading a file
handle = open('mbox-short.txt')
text = handle.read()
words = text.split()

	# Looping through a file and putting keys and values
	# in dictionary collection and counting them
counts = dict()
for word in words:
	counts[word] = counts.get(word, 0) + 1

	# Looping through a dic collection and finding out
	# most common word and count number
bigCount = None
bigWord = None
for word, count in counts.items():
	if bigCount is None or count > bigCount:
		bigWord = word
		bigCount = count
print bigWord, bigCount