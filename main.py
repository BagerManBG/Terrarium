from models.terrain import Terrain
from src.create_creatures import create_creatures

terrain = Terrain(4,5)

create_creatures(10, terrain)

terrain.status()

terrain.tick()
terrain.tick()
terrain.tick()

terrain.status()

terrain.tick()

terrain.status()