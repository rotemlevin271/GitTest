name = 'Rotem'
age = 24

print(name)
print(age + 5)

new_age = age + 5
print('your new age is : ' + str(new_age))

last_name = 'Levin'
print(name + last_name)

print('')
print('Just a quick reminder :  You cant use the "+" operator between different types of data (variables)')

print(age - 2)


############
a = 7
b = 3

if a > b and a == 3:
    print('a is bigger than b and also equals 3 (:')
if b > a:
    print('b is bigger then a !')
    if b > 3:
        print('b is also actually bigger than 3 !!')
if a == b:
    print('Wow ! they are identical !!')
elif a > b:
    print('Well I guess a is bigger than b')
# Oh man... they are not the same :(
print('! IMPORTANT !')
print('When using an "elif" statement, once the first "elif" is true (among a list of "elif"s) the program ignores any other following condition statements !')

num = int(input("Type your dog's age"))
if num > 10:
    print('Oh Im sorry..your dog is old and about to die...   ', num , ' is a lot')
    print(num * 2 , ' - thats your dogs age times two, its actually like my age')
