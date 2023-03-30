import random
import time

roll = input("Do you want to roll the dice(type yes or no) : ")
print(roll)

roll == "yes"

while roll == "yes":
    print("Rolling the dice...")
    time.sleep(1)

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print("The values are:")
    print("Dice 1 =", dice1 ,", Dice 2 = ", dice2)

    roll = input("Do you want to roll the dice again (type yes or no) : ")


