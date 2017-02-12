# Set dictionary, and find out most common word in the file

    # V.1
handle = open('mbox-short.txt')
text = handle.read()
counts = dict()

for line in text:
    if line.startswith('From '):
        words = line.split()
    print text
    # counts[word] = counts.get(word, 0) +1

# lst = list()
# for key, value in counts.items():
#     lst.append((value, key))

# lst. sort(reverse=True)

# for value, key in lst[:10]:
#     print key, value


#     # V.2
# c = {'a': 10, 'b': 1, 'c': 22}
# print(sorted([(v, k) for k, v in c.items()]))