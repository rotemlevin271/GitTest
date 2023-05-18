# Extracurriculars:
# First Class
# 1.
print('Hello, \nRotem')
# to print in 2 separate lines in one print command use \n .

# 2.
# num = input('Enter number')
# רק תרגול של שימוש באינפוט

# 3.
import sys
print('The python version is :' , sys.version)

# 4.
word = 'hello' [::-1]
print(word)

# Reversing a string is used by adding [::-1] after the string,
# like the example above

# 5.

word2 = 'what'

print(len(word2))
# The len() function gives the amount of letters in a string

# 6.

from datetime import datetime
print(datetime.now())
# The way to get and print the date and time

# 7.

# תרגיל כמו 7 נעשה כבר בשיעורי בית הרגילים.. זה קל

# 8.
x = 120
if x > 5 & x < 200:
    print('MATCH')



# Second Class

# M
rows = 6
for d in range(rows):
    for b in range(d):
        # כל עוד הפרינט בלופ ומקבל אנד חדש שאומר לו
        # לא לרדת שורה ובמקום זה לשים רווח אז הוא לא יירד שורה
        print('#', end='')
    # כשהוא מסיים להדפיס את כל הלולאה הפנימית, כדי שיירד
    # שורה לפני שיריץ את הלולאה הפנימית שוב אז
    # נעשה הדפסה ללא כלום כאשר האנד של לא להדפיס כלום זה לרדת שורה
    print('')

# N
N = 5
for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')

# O
# 1.
def getNum():
    num = input('Enter number please : ')
    return num
def sum3():
    mispar = getNum()
    sum = 0
    for digit in str(mispar):
        sum += int(digit)
    return sum
print(sum3())

