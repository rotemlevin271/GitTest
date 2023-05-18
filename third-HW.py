try:
    a = 1/0;
except:
    print('theres an error')


# 3. yes the code is legal

# 4. All types

# 5. ?
#
# 7.
my_file = open("C:/temp/README.txt",'w')
my_file.close()
# 8.
my_file = open("C:/temp/README.txt",'w')
my_file.write('rotem')
my_file.close()
# 9.
my_file = open("C:/temp/README.txt",'r')
cont = my_file.read()
print(cont)
my_file.close()

# 10.
my_file = open("C:/temp/README.txt",'w+')
my_file.write('מה נשמע ?')
my_file.close()
my_file = open("C:/temp/README.txt",'r')
cont = my_file.read()
print(cont)
my_file.close()

# 11.
from flask import Flask

app = Flask(__name__)


@app.route('/content')
def cont():
    return open("C:/temp/README.txt",'r').read() , 200 # status code

# accessed via <HOST>:<PORT>/welcome
@app.route("/register")
def register():
    open("C:/temp/README.txt",'w').write('hello')
    return "<H1 id='success'>Success!</H1>", 200 # status code

@app.route("/king")
def king():
    return "You are the queen !", 200 # status code


# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
# השורה הבאה מריצה את האתר - להוציא מקומנט
#### app.run(host='127.0.0.1', debug=True, port=30000)

# 12.
from PIL import Image, ImageFilter

im = Image.open("C:/temp/pexels-polina-kovaleva-7270551.jpg")
im.filter(ImageFilter.BLUR) # לא עבד לי לעשות פעולות על התמונה
im.show()