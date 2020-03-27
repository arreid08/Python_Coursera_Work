# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('Blast Off')

# How to find the largest number
# largest_num = None
# print('Before', largest_num)
# for i in [9, 41, 12, 3, 74, 15]:
#     if largest_num is None:
#         largest_num = i
#     elif i > largest_num:
#         largest_num = i
#     print(largest_num, i)
# print('After', largest_num)

# Count in a loop
# zork = 0
# print('Before:', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + 1
#     print(zork, thing)
# print('After', zork)

# Finding the Average in a loop
# count = 0
# sum = 0
# print('Before:', count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After', count, sum, sum / count)

# Search Using Boolean Variable, If this loop ever finds a 3, then found is True.
# found = False
# print('Before:', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)

# Find the Smallest Value
# smallest_num = None
# print('Before', smallest_num)
# for i in [9, 41, 12, 3, 74, 15]:
#     if smallest_num is None:
#         smallest_num = i
#     elif i < smallest_num:
#         smallest_num = i
#     print(smallest_num, i)
# print('After', smallest_num)

# Repeat asking for a number until the word DONE is entered
# exercise 5.1
# num = 0
# tot = 0.0
# while True:
#     sval = input('Enter a number:')
#     if sval == 'done':
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid Input')
#         continue
#     num = num + 1
#     tot = tot + fval
# print(tot, num, tot / num)

#Assignment 5.2
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        fnum = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = fnum
    elif fnum > largest:
        largest = fnum
    elif smallest is None:
        smallest = fnum
    elif fnum < smallest:
        smallest = fnum

print('Maximum is', largest)
print('Minimum is', smallest)