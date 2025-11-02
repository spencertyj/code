import random
import matplotlib.pyplot as plt

r1=random.randint(1,6)
print(r1)

def plus(a,b):
    sum = a + b
    return 

def roll_dice(num_sides, num_dice):
    total = 0

    for i in range(num_dice):
        total = total + random.randint(1,6)
    return total



dice_rolls = []
for i in range(1000):
    dice_rolls.append(roll_dice(6,3))
print(dice_rolls)

plt.hist(dice_rolls,bins ='auto')
plt.grid(axis='x',alpha=0.75)
plt.xlabel('Total Value')
plt.ylabel('Frequency')
plt.title('Dice Rolls')

plt.show()

