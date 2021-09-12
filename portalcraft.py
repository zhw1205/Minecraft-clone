from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise
from random import *
import time
from playsound import playsound
from Tree_gen import Trees
from Ruins import Ruins
from Rooms import Room
from blocks import BTYPE
life = Trees()
Old = Ruins()
Suspitious = Room()
app = Ursina()
player = FirstPersonController()
player.y = -10
player.gravity = 0.2
#player.cursor.visible = False
window.exit_button.visible = False
window.color = color.rgb(0, 130, 255)
Grass = 'grassCube.png'
GrassModel = 'GrassCube.obj'
Zombie = 'zombie.png'
Pillager = 'pillager.png'
frameTex = 'Frame'
Craft = 'crafting table Tex.png'
Brick = 'brick.png'
Sand = 'sand.png'
Log = 'log.png'
Smelt = 'furnace.png'
MossyCobble = 'mossy cobblestoneTex'

build_distance = 4

Btype = BTYPE.Grass

def input(key):
    if key == 'escape':
        quit()
    if key == 'right mouse up':
        global Btype, e
        e = Entity(model=GrassModel)
        e.collider = 'mesh'
        e.model = GrassModel
        e.texture = Btype
        e.position = floor(player.position + camera.forward * build_distance)
        e.y = e.y + 3
    if key == 'left mouse up':
        e = mouse.hovered_entity
        e.y -= 1
    else:
        pass
    if key == '1':
        Btype = BTYPE.Brick
        e.model = GrassModel
    if key == '0':
        Btype = BTYPE.Grass
        e.model = GrassModel
    if key == '2':
        Btype = BTYPE.Sand
        e.model = GrassModel
    if key == '3':
        Btype = BTYPE.Log
        e.model = GrassModel
    if key == '4':
        Btype = BTYPE.Craft
        e.model = GrassModel
    if key == '5':
        Btype = BTYPE.Smelt
        e.model = GrassModel
    if key == '6':
        Btype = BTYPE.MossyCobble
        e.model = GrassModel

def update():
    if player.y < -3:
        player.y = 10
    genPerlin(randrange(-100, 100), randrange(-100, 100))
    structures(randrange(-100, 100), randrange(-100, 100))
    genTerr()

noise = PerlinNoise(octaves=2,seed=randrange(1, 100000000000000000000000000000000000))
amp = 6
freq = 24

def genPerlin(_x, _z, plantTree=True):
    y = 1
    freq = 32
    amp = 21
    y += ((noise([_x/freq,_z/freq]))*amp)
    if plantTree==True:
        life.checkTree(_x,y,_z)

def structures(_x, _z, genRuins=True, genRoom=True):
    y = 1
    freq = 32
    amp = 21
    y += ((noise([_x/freq,_z/freq]))*amp)
    if genRuins==True:
        Old.checkRuins(_x,y,_z)
    if genRoom==True:
        Suspitious.checkRoom(_x,y,_z)

shells = []
shellWidth = 12
for i in range(shellWidth*shellWidth):
    ent = Entity(model=GrassModel, texture=Grass, collider='box')
    shells.append(ent)

def genTerr():
    global amp, freq
    for i in range(len(shells)):
        x = shells[i].x = floor((i/shellWidth) + player.x - 0.5*shellWidth)
        z = shells[i].z = floor((i%shellWidth) + player.z - 0.5*shellWidth)
        y = shells[i].y = floor(noise([z/freq, x/freq])*amp)

x = shells[i].x = floor((i/shellWidth) + player.x - 0.5*shellWidth)
z = shells[i].z = floor((i%shellWidth) + player.z - 0.5*shellWidth)
ZombieModel = 'pillager.obj'
pillager = Entity(model=ZombieModel, texture=Pillager, scale=1, double_sided=True, collider='mesh')

app.run()