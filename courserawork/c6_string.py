# typical code with a while loop.
# fruit = 'banana'
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1

#same code as above but more clear and concise
# fruit = 'banana'
# for letter in fruit:
#     print(letter)

# slicing 
# s = 'Monty Python'
# print(s[0:4])
# the above is start at 0 and go up to but NOT including 4
# answer is Mont
#print(s[6:7])
# answer is P
#print(s[6:20])
# answer is Python, it's ok that the number goes beyond the range of the string, this will not cause an error.
#print(s[:2])
#Mo

## Concatenation
# a = 'Hello'
# b = a + 'There'
# print(b)
#answer HelloThere (with no space)
# c = a + ' ' + 'There'
# print(c)
# answer Hello There (with a space)

# fruit = 'banana'
# 'n' in fruit
# in is an operator to say is the letter in the word.
# answer True
# 'm' in fruit
# answer False
# 'nan' in fruit
#  answer True.
#if 'a' in fruit:
#    print('Found it')

##String Comparison
# word = banana
# if word == 'banana':
#     print('All right, bananas.')
# if word < 'banana':
#     print('Your Word,' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word,' + word + ', comes before banana.')

# Assignment 6.5, find the number and convert it form a string to a number.
text = "X-DSPAM-Confidence:    0.8475"
snum = text.find('0')
num = text[snum : ]
fnum = float(num)
print(fnum)