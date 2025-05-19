import random, os

#numbers locked
x=""
tries=0

while True:
    os.system("cls")

    tries+=1

    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)

    #question
    print(f"your number is {x} pick a number:",a,b,c)

    #number picked
    num=str(input())

    while len(num)>1 or int(num)!=a or int(num)!=b or int(num)!=c :
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,9)

        os.system("cls")

        print("wrong, try again")

        #question
        print(f"your number is {x} pick a number:",a,b,c)

        #number picked
        num=str(input())

    x=x+num
