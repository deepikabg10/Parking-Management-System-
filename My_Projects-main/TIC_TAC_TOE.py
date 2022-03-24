import numpy as np
n=np.array([["1","2","3"],["4","5","6"],["7","8","9"]])
pla1=input("Enter player 1 name : ")
pla2=input("Enter player 2 name : ")
sym1=input("Enter the symbol of player 1 : ")
sym2=input("Enter the symbol of player 2 : ")
def position(pos,n,sym):
    if pos==1:
        n[0][0]=sym
    elif pos==2:
        n[0][1]=sym
    elif pos==3:
        n[0][2]=sym
    elif pos==4:
        n[1][0]=sym
    elif pos==5:
        n[1][1]=sym
    elif pos==6:
        n[1][2]=sym
    elif pos==7:
        n[2][0]=sym
    elif pos==8:
        n[2][1]=sym
    else:
        n[2][2]=sym
    print(n)
print("Layout : \n",n)
l=[]
i=0
while i<9:
    if i%2==0:
        pos=int(input("{},please enter the position required (1-9) : ".format(pla1)))
        position(pos,n,sym1)
        for j in range(3):
            k=0
            if n[j][k]==n[j][k+1]==n[j][k+2]==sym1 or n[k][j]==n[k+1][j]==n[k+2][j]==sym1:
                print("{}, won the match, score = {}".format(pla1,10))
                i=9
            elif n[0][0]==n[1][1]==n[2][2]==sym1 or n[0][2]==n[1][1]==n[2][0]==sym1:
                print("{}, won the match, score = {}".format(pla1,10))
                i=9
    else:
        pos=int(input("{},please enter the position required (1-9) : ".format(pla2)))
        position(pos,n,sym2)
        for j in range(3):
            k=0
            if n[j][k]==n[j][k+1]==n[j][k+2]==sym2 or n[k][j]==n[k+1][j]==n[k+2][j]==sym2:
                print("{}, won the match, score = {}".format(pla2,10))
                i=9
            elif n[0][0]==n[1][1]==n[2][2]==sym2 or n[0][2]==n[1][1]==n[2][0]==sym2:
                print("{}, won the match, score = {}".format(pla2,10))
                i=9
    
    i=i+1
last=print("Thank you")
