from random import randint

class Die():

	def __init__(self):
		self.sides = int(input("PLEASE input the sides of your roll: "))

	def roll_die(self):
		print("\nThe random number is :" + str(randint(1,self.sides)))
		

my_roll= Die()

for i in range(1,10):
	my_roll.roll_die()
	i += 1

