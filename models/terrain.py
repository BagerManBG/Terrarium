from models.cell import Cell

class Terrain:
	def __init__(self, size_x, size_y):
		self.cells = []
		self.size_x = size_x
		self.size_y = size_y

		print('\n')
		print('Terrain created with dimensions: %(x)dx%(y)d.' %{
			'x': self.size_x,
			'y': self.size_y
		})

		self.initialize_field()

	def tick(self):
		creatures = []
		for i in range(0, len(self.cells)):
			creatures += self.cells[i].creatures

		for i in range(0, len(creatures)):
			creatures[i].move(self)

	def status(self):
		print('\n', '------------------------------------------------------', '\n')
		for i in range(0, self.size_x * self.size_y):
			print('Cell #%(n)d (%(t)s) at (%(x)dx%(y)d)' %{
				'n': i,
				't': self.cells[i].get_cell_type(),
				'x': self.cells[i].x,
				'y': self.cells[i].y
			})
			self.cells[i].list_creatures()
			print('\n')
		
	def initialize_field(self):
		print('\n')
		for i in range(0, self.size_x):
			for j in range(0, self.size_y):
				self.cells.append(Cell(i, j))