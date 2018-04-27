import random

class Cell():
	cell_types = ['grass', 'mountain', 'desert', 'water']
	creatures = []

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.cell_type = random.randrange(0, 4)
		print ('A %(type)s field created at (%(x)dx%(y)d)' %{
			'type': self.getCellType(),
			'x': self.x,
			'y': self.y
		})

	def listCreatures():
		pass

	def countDeadCreatures():
		pass

	def countAliveCreatures():
		pass
		
	def getCellType(self):
		return self.cell_types[self.cell_type]