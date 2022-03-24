import random
s=random.randint(30,1000)
n=random.randint(s-31,s-1)
m=random.randint(s+1,s+31)
def prime(a):
    b=0
    for l in range(1,a+1):
        if a%l==0:
            b=b+1
    if b==2:
        return 1
    else:
        return 0
def result(n,s,ch_cou):
    if n==s:
        print("The number you had guessed is correct")
        return 1,ch_cou-1
    if n!=s:
        print("The number you have guessed is incorrect")
    if ch_cou>7:
        choice=int(input("To get one more hint press 1,else print any other number, if u take one more hint maximum no. of chances will be reduced by 2 chances : "))
    else:
        choice=0
    if n!=s:
        if choice==1:
            if s%5==0:
                print("The number is an multiple of 5")
            elif s%4==0:
                print("The number is an multiple of 4")
            elif s%3==0:
                print("The number is an multiple of 3")
            elif s%7==0:
                print("The number is an multiple of 7")
            pri=prime(s)
            if pri==True:
                print("The number is a prime number")
            ch_cou=ch_cou-3
            print("Chances remaining = ",ch_cou)
        else:
            ch_cou=ch_cou-1
            print("Chances remaining = ",ch_cou)
        return 0,ch_cou
print("Hint : \nThe number lies in between {} and {}".format(n,m))
if s%2==0:
    print("The number is an even number")
else:
    print("The number is an odd number")
ch_cou=10
print("Maximum no.of chances = 10")
i=0
while i<10:
    inp=int(input("Enter the number you guessed : "))
    fun=result(inp,s,ch_cou)
    ch_cou=fun[1]
    if fun[0]==True:
        print("Maximum no. of chances taken to guess the number is : ",10-fun[1])
        i=11
    if ch_cou==0:
        print("Thank you")
        print("You didn't guess the number correctly and the number is",s)
        i=11
    i=i+1
