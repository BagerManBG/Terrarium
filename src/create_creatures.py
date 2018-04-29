from models.carnivore import Carnivore
from models.herbivore import Herbivore
from models.scavanger import Scavanger
import random

def create_creature(id, x, y, cr_type):
	if cr_type == 0:
		return Carnivore(id, x, y)
	elif cr_type == 1:
		return Herbivore(id, x, y)
	else:
		return Scavanger(id, x, y)

def create_creatures(num, terrain):
	for i in range(0, num):
		rand = random.randrange(0, len(terrain.cells))

		while terrain.cells[rand].get_cell_type() == 'water':
			rand = random.randrange(0, len(terrain.cells))
			
		x = terrain.cells[rand].x
		y = terrain.cells[rand].y
		cr_type = random.randrange(0, 3)
		terrain.cells[rand].creatures.append(create_creature(i, x, y, cr_type))