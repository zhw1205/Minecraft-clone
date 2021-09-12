from perlin_noise import PerlinNoise
from ursina import Entity, color, Vec3
from random import randrange
Log = 'log.png'
GrassModel = 'GrassCube.obj'
class Trees:
    def __init__(this):
        this.noise = PerlinNoise(seed=4)

    def checkTree(this, _x,_y,_z):
        freq = 5
        amp = 100
        treeChance = ((this.noise([_x/freq,_z/freq]))*amp)
        if treeChance > 20:
            this.plantTree(_x,_y,_z)

    def plantTree(this,_x,_y,_z):
        from random import randint
        tree = Entity(  model = None,
                        position=Vec3(_x,_y,_z))
        global trunk
        trunk = Entity( model=GrassModel,texture=Log,scale_y = randrange(5, 10),collider='box')
        crown = Entity( model='cube',scale=10,y=trunk.y+trunk.scale_y,texture='leaves.png')
        crown.parent=tree
        trunk.parent=tree
        tree.y = 3