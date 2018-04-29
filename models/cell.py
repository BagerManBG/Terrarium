import random

class Cell():
	cell_types = ['grass', 'mountain', 'desert', 'water']

	def __init__(self, x, y):
		self.creatures = []
		self.x = x
		self.y = y
		self.cell_type = random.randrange(0, 4)
		print ('A %(type)s field created at (%(x)dx%(y)d)' %{
			'type': self.get_cell_type(),
			'x': self.x,
			'y': self.y
		})

	def list_creatures(self):
		print('Alive creatures: %(alive)d, Dead creatures: %(dead)d' %{
			'alive': self.count_alive_creatures(),
			'dead': self.count_dead_creatures()
		})

		num_creatures = len(self.creatures)
		if num_creatures == 0:
			print('No creatures in this cell')
		else:
			for i in range(0, num_creatures):
				print('A %(age)s-year-old %(type)s (#%(n)d)' %{
					'age': self.creatures[i].age,
					'type': self.creatures[i].cr_type,
					'n': self.creatures[i].id
				})

	def count_alive_creatures(self):
		count = 0
		for i in range(0, len(self.creatures)):
			if self.creatures[i].alive:
				count += 1
		return count

	def count_dead_creatures(self):
		count = 0
		for i in range(0, len(self.creatures)):
			if not self.creatures[i].alive:
				count += 1
		return count
		
	def get_cell_type(self):
		return self.cell_types[self.cell_type]