import random
def dice_roll():
    x = random.randrange(1,7)
    y = random.randrange(1,7)
    print(str("dice one ") + str(x))
    print(str("dice two ") + str(y))
    print("you rolled " + str(x+y))
dice_roll()
