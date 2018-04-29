from models.creature import Creature

class Herbivore(Creature):
	def __init__(self, id, x, y):
		super().__init__(id, x, y)
		self.cr_type = 'Herbivore'
		