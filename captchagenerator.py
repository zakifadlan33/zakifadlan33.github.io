import string
import random
from turtle import width
from captcha.image import ImageCaptcha
#random name
namacaptcha = []
for x in range(14):
    letter = string.ascii_lowercase
    a= str(''.join(random.choice(letter)))
    letter = string.ascii_uppercase
    b= str(''.join(random.choice(letter)))
    letter = string.ascii_letters
    c= str(''.join(random.choice(letter)))
    letter = string.digits
    d= str(''.join(random.choice(letter)))
    nama = a+b+c+d
    namacaptcha.append(nama)   
#captcha
image = ImageCaptcha(width=280,height=90)
data = image.generate(nama)
y=0
for x in namacaptcha:
    image.write(x,"images/"+x+".jpg")
    y+=1
    print(y)

