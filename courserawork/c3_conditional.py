# x = 5
# if x == 5:
#     print('Equals 5')
# if x > 4:
#     print('Greater than 4')
# if x >= 5:
#     print('Greater than or Equal to 5')
# if x < 6:
#     print('Less than 6')
# if x <= 5:
#     print('Less than or Equal to 5')
# if x != 6:
#     print('Not equal to 6')

# x = 20 
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# else:
#     print('Large')

# print('All Done')

#3.1 Assignment Answer
# hrs = input("Enter Hours:")
# rate = input("Rate:")
# h = float(hrs)
# r = float(rate)
# if h > 40:
#     overh = h % 40
#     overpay = r * 1.5 * overh
#     standard_pay = 40 * r
#     total = standard_pay + overpay
#     print(total)
# else:
#     print('No overtime.')

#3.3 Assignment Answer
scoreinp = input('Enter Score:')
score = float(scoreinp)
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
else:
    print('F')