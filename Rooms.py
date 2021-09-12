from perlin_noise import PerlinNoise
from ursina import Entity, color, Vec3
from random import randrange
from blocks import BTYPE
Log = 'log.png'
GrassModel = 'GrassCube.obj'
class Room:
    def __init__(this):
        this.noise = PerlinNoise(seed=randrange(1, 1000))

    def checkRoom(this, _x,_y,_z):
        freq = 5
        amp = 100
        treeChance = ((this.noise([_x/freq,_z/freq]))*amp)
        if treeChance > 50:
            this.genRoom(_x,_y,_z)

    def genRoom(this,_x,_y,_z):
        Room = Entity(  model = None,
                        position=Vec3(_x,_y,_z))
        wall = Entity( model=GrassModel,texture=Log,scale_y=7, scale_x=7,collider='mesh')
        wall2 = Entity(model=GrassModel,texture=Log,scale_y=7, scale_z=7,collider='mesh', x=4, z=4)
        wall3 = Entity(model=GrassModel,texture=Log,scale_y=7, scale_z=7,collider='mesh', x=-4, z=4)
        Doorway = Entity(model=GrassModel,texture=Log,scale_y=7, scale_z=3,collider='mesh', z=4, rotation_y = 90)
        wall.parent = Room
        wall2.parent = Room
        wall3.parent = Room
        Doorway.parent = Room
        Room.y = 2