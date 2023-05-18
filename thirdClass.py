try:
    my_file = open("C:\‏‏תיקיה חדשה\README.txt",'r')
    content = my_file.read()
    # content = my_file.write('123')
    print(content)
except IOError as e:
    print('the error is : ' , e)
print('program stil running .. !')
# my_file = open("C:\‏‏תיקיה חדשה\README.txt.txt",'r+')
# content = my_file.write('text to add ')
#
# my_file = open("C:\‏‏תיקיה חדשה\README.txt.txt",'a')
# content = my_file.write('hello, ')
# content = my_file.write('the monkey ')
#
# my_file = open("C:\‏‏תיקיה חדשה\README.txt.txt",'a','encoding=utf-8')
# content = my_file.write('loves bananas ')
# my_file.close()

# חשוב לעשות סגירה לקבצים כדי לשחרר אותו מהזיכרון ולייעל את הזיכרון !
# כדי שהקובץ ייסגר אוטומטית במקום שנעשה סגירה ידנית עם הפעולה close
# ניתן לכתוב בצורה הבאה :
with open('file_path','w') as x:
    x.write('hello')
# על ידי שימוש בwith תמיד יסגר הקובץ בסוף

# my_file = open("C:\‏‏תיקיה חדשה\README.txt.txt",'x')
# content = my_file.write('mmadonaa')

