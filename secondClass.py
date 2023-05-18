for t in range(5):
    print(t)
# הערך השני(או היחיד כשנמצא לבד) הוא כמות הפעמים שירוץ הפור
# אם נותנים שני מספרים אז הערך הראשון בעצם מחליף את הערך ההתחלתי של איקס במקום 0 שהוא הדיפולט
# להוסיף מספר שלישי יחליף את מספר התקדמות האיטרציה בכל הרצה של הלולאה עד סופה במקום הדיפולט שהוא ב-1

oshri = 'love'
# while oshri == 'love':
#     print('Oshri is my love')
#     oshri = input('Enter new compliment')
#     print('Goodbye , gorgeous')

# break statement - עוצר כל לולאה ויוצא ממנה
# continue statement - מרגע ההשמה זה ישר מקפיץ את הלולאה לאיטרציה הבאה שלה(מבלי לבצע את מה שמופיע אחרי הקונטיניו)
# shift + tab - מחזיר טאב אחד אחורה


def multiply(x, y):
    return x*y

def averageSum(x, y, z):
    return ((x+y+z)/3)

print(averageSum(5,5,6))

def greetUser(Uname):
    return 'Greetings ' + Uname + ' !'

print(greetUser('Rotem'))

# כדי להשתמש במודול חיצוני צריך לבצע לו קודם import

import datetime

# List

list = [5,'a',True]
list.insert(1,7)  #משמאל אתה אומר לו באיזה אינדקס ומימין את הערך שיהיה לו
print(list)
list.append(12)   # מוסיף מהסוף איבר לרשימה
print(list)
list.pop(0)       # מסיר איבר ממיקום מסוים ברשימה
print(list)
list[0] = 33      # מחליף את הערך של איבר במיקום 0 ברשימה
print('list is ' , len(list) , ' items long')

for temp in list:
    print(temp)
# שני הפורים נותנים את אותה תוצאה ,העליון הוא תצורת כתיבה קצרה יותר
for i in range(len(list)):
    print(list[i])

# Tuple - כמו רשימה רק שלא ניתן לעשות עליה פעולות
# האיברים שלה נשארים קבועים
# עדיף להשתמש בתו-פל ככל שניתן - מונע טעויות, שליפה מהירה יותר של איברים
tuple = 1, 2, 3
tuple2 = ('a', 'b', 'z')   # זה הסינתקס

# Dictionary - key:value pairs
dictionary = {'a':1, 'b':2}
dictionary['a'] = 3   # משנה value ל-key מסוים
del(dictionary['a'])  # מוחק איבר שלם
print(dictionary.keys()) / print(dictionary.values())  # 2 דרכים להדפיס את ערכי המילון

