from models.creature import Creature

class Scavanger(Creature):
	def __init__(self, id, x, y):
		super().__init__(id, x, y)
		self.cr_type = 'Scavanger'
		self.hunger_step = 10

	def feed(self, terrain, current_cell_id):
		pass