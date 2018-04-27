from models.cell import Cell

class Terrain:
	cells = []

	def __init__(self, size_x, size_y):
		self.size_x = size_x
		self.size_y = size_y

		print('\n')
		print('Terrain created with dimensions: %(x)dx%(y)d.' %{'x': self.size_x, 'y': self.size_y})

		self.initializeField()

	def tick():
		pass

	def status(self):
		print('\n')
		for i in range(0, self.size_x * self.size_y):
			print (self.cells[i].getCellType(), self.cells[i].x, self.cells[i].y)
		
	def initializeField(self):
		print('\n')
		for i in range(0, self.size_y):
			for j in range(0, self.size_x):
				self.cells.append(Cell(i, j))