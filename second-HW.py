# A
x = 5
y = 6

if x > y:
    print('BIG')
elif x < y:
    print('small')

# B
for i in range(5):
    print(i)

# C
# היה כבר בשיעורי בית הקודמים

# D
# 1. The loop will run 10 times 2. The last number to be printed will be 10
cou = 1
while cou<11:
    print(cou)
    cou=cou+1

# E
my_dictionary = {'age':24 ,'firstLett':'l', 'cur':3.4, 'hul':True, 'apartN':31}
print(my_dictionary)
print(my_dictionary['age'] + my_dictionary['cur'])

# F
cellNum = input('Enter your phone number : ')
print('phone number : ' , cellNum)

# G
# 1.
def printHello():
    print('hello')
# 2.
def calculate():
    print(5+3.2)
calculate()

# H
# 1.
def printName(name):
    print(name)
printName('rotem')

# 2.
def devByTwo(num):
    print(num / 2)
devByTwo(16)

# I
# 1.
def sum(w,e):
    print(w+e)
sum(1,2)

# 2.
def addSpace(name1,name2):
    print(name1 + ' ' + name2)
addSpace('hello','mom')

# J
my_list = [2,4,6]
for x in my_list:
    print(x)

# K
def sum2(list):
    summ = 0
    for i in list:
        summ += i
    print(summ)
sum2([3,3,3,3])

# L
for i in my_dictionary.keys():
    print(i)



