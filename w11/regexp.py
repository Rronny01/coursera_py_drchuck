# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end


# Python Regular Expression Quick Guide

# ^        Matches the beginning of a line
# $        Matches the end of the line
# .        Matches any character
# \s       Matches whitespace
# \S       Matches any non-whitespace character
# *        Repeats a character zero or more times
# *?       Repeats a character zero or more times
#          (non-greedy)
# +        Repeats a character one or more times
# +?       Repeats a character one or more times
#          (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (        Indicates where string extraction is to start
# )        Indicates where string extraction is to end


# extract from line
import re
lin = 'From stephen.marqueezardus@uct.az.moz Sat Jan 5 09:12:19 2009'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)

# '\S+?@\S+

# import re
# hand = open('mbox-short.txt')
# numList = list()
# for line in hand():
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(stuff) != 1: continue
#     num = float(stuff[0])
#     numList.append(num)
# print('Maximum:', max(numList))

