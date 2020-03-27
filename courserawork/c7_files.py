# fhand = open('mbox-short.txt')
# 	# This line will access a file.
# inp = fhand.read()
# 	# This line will read the file into a single string to inp.
# print(len(inp))
# 	# This line will print the total number of characters.
# print(inp[ : 20])
#     # This line will print characters 0-19

# Assignment 7.1 Input the file Word.txt and print the contents in uppercase.
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     strip = line.strip()
#     upper = strip.upper()
#     print(upper)

# Assignment 7.2 Input the file mbox-short.txt. 
fname = input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = str(line)
    find = str.find(line, '.') - 2
    find = line[find : ]
    find = float(find)
    y = find + y
    x = x + 1
    avg = y/x
    avg = float(avg)
print('Average spam confidence:', avg)