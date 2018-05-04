import random

class Creature():
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y
		self.age = 1
		self.alive = True
		self.hunger = 100
		self.hunger_step = 20
		self.possible_moves = [True, True, True, True]

	def feed(self, terrain, current_cell_id):
		pass

	def move(self, terrain):
		print(self.id, self.get_alive(terrain), self.hunger)
		if self.get_alive(terrain):
			if self.hunger <= 60:
				self.get_possible_moves(terrain.size_x, terrain.size_y, self.x, self.y)
				rand = random.randrange(0, 4)

				while not self.possible_moves[rand]:
					rand = random.randrange(0, 4)

				if rand == 0:
					new_x = self.x
					new_y = self.y - 1
				elif rand == 1:
					new_x = self.x + 1
					new_y = self.y
				elif rand == 2:
					new_x = self.x
					new_y = self.y + 1
				else:
					new_x = self.x - 1
					new_y = self.y

				current_cell_id = self.get_cell_id(terrain.size_y, self.x, self.y)
				next_cell_id = self.get_cell_id(terrain.size_y, new_x, new_y)

				if terrain.cells[next_cell_id].get_cell_type == 'water':
					self.alive = False

				terrain.cells[next_cell_id].creatures.append(self)

				print(self.alive)

				for i in range(0, len(terrain.cells[current_cell_id].creatures)):
					if terrain.cells[current_cell_id].creatures[i].id == self.id:
						terrain.cells[current_cell_id].creatures.pop(i)
						break

				print('A %(t)s (%(n)d) moved from (%(x)dx%(y)d) to (%(new_x)dx%(new_y)d)' %{
					't': self.cr_type,
					'n': self.id,
					'x': self.x,
					'y': self.y,
					'new_x': new_x,
					'new_y': new_y
				})

				self.feed(terrain, current_cell_id)

			self.hunger -= self.hunger_step

	def get_alive(self, terrain):
		for i in range(0, len(terrain.cells)):
			for j in range(0, len(terrain.cells[i].creatures)):	
				if terrain.cells[i].creatures[j].id == self.id:
					return terrain.cells[i].creatures[j].alive

	def get_cell_id(self, size_y, x, y):
		return x * size_y + y

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