import random
import string
print("1. Easy letters password\n2. Easy digits password\n3. Medium password\n4. Strong password")
n=int(input("Enter the difficulty level of the password required : "))

def easy_password_letters():
    pat=string.ascii_letters
    cou=int(input("Enter length of each password : "))
    num=int(input("Enter number of passwords required : "))
    for i in range(num):
        password=random.sample(pat,cou)
        str1=""
        for i in range(cou):
            str1=str1+password[i]
        print(str1)

def easy_password_digits():
    pat=string.digits
    cou=int(input("Enter length of each password : "))
    num=int(input("Enter number of passwords required : "))
    for i in range(num):
        password=random.sample(pat,cou)
        str1=""
        for i in range(cou):
            str1=str1+password[i]
        print(str1)

def medium_password():
    pat=string.ascii_lowercase+string.ascii_uppercase+string.digits
    cou=int(input("Enter length of each password : "))
    num=int(input("Enter number of passwords required : "))
    for i in range(num):
        password=random.sample(pat,cou)
        str1=""
        for i in range(cou):
            str1=str1+password[i]
        print(str1)

def strong_password():
    pat=string.printable
    cou=int(input("Enter length of each password : "))
    num=int(input("Enter number of passwords required : "))
    for i in range(num):
        password=random.sample(pat,cou)
        str1=""
        for i in range(cou):
            str1=str1+password[i]
        print(str1)

if n==1:
    easy_password_letters()
elif n==2:
    easy_password_digits()
elif n==3:
    medium_password()
elif n==4:
    strong_password()
else:
    print("Enter valid choice")
    exit
