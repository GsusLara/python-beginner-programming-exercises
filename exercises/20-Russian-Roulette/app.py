import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    condition=spin_chamber()
    if (condition == bullet_position):
        alert="You are dead!"
    else:
        alert="Keep playing!"

    return (alert)


print(fire_gun())