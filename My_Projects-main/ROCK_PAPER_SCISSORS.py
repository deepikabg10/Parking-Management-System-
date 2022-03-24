import random
print("Rock Paper Scissors Game")
print("Rules:\nRule - 1.You need to use\n1 - for Rock\n2 - for Paper\n3 - for Scissors\nRule -2. You can play only 20 rounds at max")
user=computer=0
for i in range(20):
    print("Round no :{}".format(i+1))
    print("1.Rock\n2.Paper\n3.Scissors\n4.exit")
    n=int(input("Enter your choice :"))
    if n==1:
        k=random.randint(1,3)
        if k==2:
            user=user+0
            computer=computer+10
            print("You have lost the game as the paper beats the rock and your score : ",user)
            print("Computer had won the  game and computer's score : ",computer)
        elif k==3:
            user=user+10
            computer=computer+0
            print("You have won the game as the paper beats the rock and your score : ",user)
            print("Computer had lost the  game and computer's score : ",computer)
        elif k==n:
            print("Both user and computer opted the same, so this is a tie match and score of user : {}, score of computer : {}".format(user,computer))
    elif n==2:
        k=random.randint(1,3)
        if k==1:
            user=user+10
            computer=computer+0
            print("You have won the game as the paper beats the rock and your score : ",user)
            print("Computer had lost the  game and computer's score : ",computer)
        elif k==3:
            user=user+0
            computer=computer+10
            print("You have lost the game as the scissors beats the paper and your score : ",user)
            print("Computer had won the  game and computer's score : ",computer)
        elif k==n:
            print("Both user and computer opted the same, so this is a tie match and score of user : {}, score of computer : {}".format(user,computer))
    elif n==3:
        k=random.randint(1,3)
        if k==1:
            user=user+0
            computer=computer+10
            print("You have lost the game as the rock beats the scissors and your score : ",user)
            print("Computer had won the  game and computer's score : ",computer)
        elif k==2:
            user=user+10
            computer=computer+0
            print("You have won the game as the scissors beats the paper and your score : ",user)
            print("Computer had lost the  game and computer's score : ",computer)
        elif k==n:
            print("Both user and computer opted the same, so this is a tie match and score of user : {}, score of computer : {}".format(user,computer))
    elif n==4 or i==19:
        print("Thank you")
        break
