# # create an empty list
# stuff = list()
# # add items to the list.
# stuff.append('book')
# # stuff.append(99)
# # print(stuff)
# stuff.append('cookie')
# stuff.append('equal')
# stuff.append('apple')
# # print(stuff)
# # sort the list in alphabetical order
# stuff.sort()
# # print the list.
# print(stuff)

# the following two examples will provide the same output.
# Find the Average
# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Average:', average)

# Find the Average using Max and Min
# main issue with this example is that this requires that you store the numbers.  
# so if you have a lot of numbers, you will use a lot of memory.
# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print('Average:', average)


#### Lists and Strings together!
# this is the more common work we will do.
# split()
# # here we take a string and turn it into a list.
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# # result: ['With', 'three', 'words']
# print(len(stuff))
# # result: 3
# print(stuff[0])
# # result: with
# for w in stuff:
#     print(w)
# # result: With
# #three
# #words

# You can tell a split to split based on a given character too.  
# split() will split based on a space.
# split(';') will split based on a ;

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From ') :
#         continue
#     #this line will split out the From line based on spaces
#     words = line.split()
#     print(words[2])
#     email = words[1]
#     # this line will split out the second item in the words list by the @ sign.
#     pieces = email.split('@')
#     print(pieces[1])

# Assignment 8.4  Return a list of words from the file.  only return words one time and sort them.
# fname = ("romeo.txt")
# fh = open(fname)
# words = list()
# b=0
# for line in fh:
#     # remove white space at the right of the text
#     line_words = line.rstrip()
#     # split each word.  Now you have a list of words in line_words.
#     line_words = line.split()
#     count = 0
#     for i in line_words:
#         # Because i comes back as an array instead of a string,
#         # we need to call out each item in the array.
#         b = line_words[count]
#         count = count + 1
#         if (i not in words):
#             words.append(b)
#             words.sort()
# print(words)

# Assignment 8.5 find all the lines that start with the word 'From
# Split() the from line and print out the second word in each line.
fname = ("mbox-short.txt")
fh = open(fname)
words = list()
count = 0
for line in fh:
    lsplit = line.rstrip()
    lsplit = line.split()
    if line.startswith('From:'):
        print(lsplit[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")