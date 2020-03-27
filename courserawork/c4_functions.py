# A Function is a variable that holds code.
# def thing():
#     print('Hello')
#     print('Fun')

# this line calls the function to run.
# thing()

#Lesson example
# def greet(lang):
#     if lang == 'es':
#         return 'Hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'

# print(greet('en'), 'Glenn')
# print(greet('es'), 'Sally')
# print(greet('fr'), 'Michael')

# 4.6 Assignment Answer
def computepay(h,r):
    if h > 40:
    	overh = h % 40
    	overpay = r * 1.5 * overh
    	standard_pay = 40 * r
    	total = standard_pay + overpay
    	return total
    else:
    	return 'No overtime.'
        
hrs = input("Enter Hours:")
rate = input("Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay",p)