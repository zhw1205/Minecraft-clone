from perlin_noise import PerlinNoise
from ursina import Entity, color, Vec3
from random import randrange
MossyCobble = 'mossy cobblestoneTex'
GrassModel = 'GrassCube.obj'
class Ruins:
    def __init__(this):
        this.noise = PerlinNoise(seed=randrange(1, 1000))

    def checkRuins(this, _x,_y,_z):
        freq = 5
        amp = 100
        treeChance = ((this.noise([_x/freq,_z/freq]))*amp)
        if treeChance > 30:
            this.genRuins(_x,_y,_z)

    def genRuins(this,_x,_y,_z):
        ruin = Entity(  model = None,
                        position=Vec3(_x,_y,_z))
        base = Entity( model=GrassModel,texture=MossyCobble,scale_y = 2,collider='box')
        base.parent=ruin
        ruin.y = 2