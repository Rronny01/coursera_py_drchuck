
fhand = open('mbox-short.txt')
counts = dict()
time = list()
lst = list()

for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    pieces = words[5].split(':')
    time.append(pieces[0])

for word in time:
    counts[word] = counts.get(word, 0) + 1

for key, value in counts.items():
    lst.append((value, key))
lst.sort(reverse=True)

for value, key in lst[:10]:
    print key, value