import random, math


def roll_the_dice():
    a = int(math.ceil(random.random()*100))
    b = int(math.ceil(random.random()*100))

    return abs(a-b)

rolls = 1000000
total = 0

for i in range(rolls):
    total += roll_the_dice()

print total/rolls
