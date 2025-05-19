import random

#numbers locked
x=""
tries=0

while True:
    tries+=1

    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)

    #question
    print(f"your number is {x} pick a number:",a,b,c)

    #number picked
    num=str(input())

    x=x+num
