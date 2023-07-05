import random
num=random.randrange(1,25)
print(num)
chances=0
while chances<6:
    guess=int(input("enter your guess\n"))
    chances+=1
    if guess==num:
        print(f"bravo your guess is correct the number is {num}")
        break
    elif guess>num:
        print("too high")
    elif guess<num:
        print("too low")
    else:
        print("please enter the number")


