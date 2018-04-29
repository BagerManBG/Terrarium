import random

class Creature():
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y
		self.age = 1
		self.alive = True
		self.hunger = 1.
		self.possible_moves = [True, True, True, True]

	def eat():
		pass

	def move(self, terrarium):
		self.get_possible_moves(terrarium.size_x, terrarium.size_y, self.x, self.y)
		rand = random.randrange(0, 4)

		while not self.possible_moves[rand]:
			rand = random.randrange(0, 4)

		#todo: get next cell and move
		#      decrease hunger
		#      if hunger < 60% -> eat

	def get_possible_moves(self, size_x, size_y, x, y):
		if y - 1 < 0:
			self.possible_moves[0] = False
		else:
			self.possible_moves[0] = True

		if x + 1 > size_x - 1:
			self.possible_moves[1] = False
		else:
			self.possible_moves[1] = True

		if y + 1 > size_y - 1:
			self.possible_moves[2] = False
		else:
			self.possible_moves[2] = True

		if x - 1 < 0:
			self.possible_moves[3] = False
		else:
			self.possible_moves[3] = True