from models.creature import Creature

class Carnivore(Creature):
	def __init__(self, id, x, y):
		super().__init__(id, x, y)
		self.cr_type = 'Carnivore'
		