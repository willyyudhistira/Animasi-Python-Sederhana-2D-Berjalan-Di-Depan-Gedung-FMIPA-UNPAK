from ursina import *
from ursina.shaders import basic_lighting_shader
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

jendela1 = Entity(model="cube", collider='box', position=(4, 1.7, -2), scale=(1.2, .5, .2), color=color.black, shader=basic_lighting_shader)
jendela2 = Entity(model="cube", collider='box', position=(2, 1.7, -2), scale=(1.2, .5, .2), color=color.black, shader=basic_lighting_shader)
jendela3 = Entity(model="cube", collider='box', position=(0, 1.7, -2), scale=(1.2, .5, .2), color=color.black, shader=basic_lighting_shader)
jendela4 = Entity(model="cube", collider='box', position=(-2, 1.7, -2), scale=(1.2, .5, .2), color=color.black, shader=basic_lighting_shader)
jendela5 = Entity(model="cube", collider='box', position=(-4, 1.7, -2), scale=(1.2, .5, .2), color=color.black, shader=basic_lighting_shader)

cube1 = Entity(model="cube", collider='box', position=(0, 3.1, 0), scale=(11.5, .1, 5), rotation=(0, 0, 0), texture="asset/light_green", shader=basic_lighting_shader)
cube2 = Entity(model="cube", collider='box', position=(0, 2.1, 0), scale=(10, 1.8, 4), rotation=(0, 0, 0), texture="asset/gray", shader=basic_lighting_shader)
cube3 = Entity(model="cube", collider='box', position=(0, .6, 0), scale=(8.5, 1.2, 3), rotation=(0, 0, 0), texture="asset/purple", shader=basic_lighting_shader)
cube4 = Entity(model="cube", collider='box', position=(0, 0, 0), scale=(10, .1, 4), rotation=(0, 0, 0), color=color.white, shader=basic_lighting_shader)
cube5 = Entity(model="cube", collider='box', position=(0, -.6, 0), scale=(8.5, 1.2, 3), rotation=(0, 0, 0), texture="asset/light_green", shader=basic_lighting_shader)
cube6 = Entity(model="cube", collider='box', position=(0, -1.6, 0), scale=(8.5, 1.2, 3), rotation=(0, 0, 0), texture="asset/light_green", shader=basic_lighting_shader)

pagar = Entity(model="cube", collider='box', position=(0, .5, -2), scale=(9.8, .05, .2), rotation=(0, 0, 0), color=color.white, shader=basic_lighting_shader)

ac1 = Entity(model="cube", collider='box', position=(2.7, -.9, -1.2), scale=(3.2, .7, 1), texture="asset/gray", shader=basic_lighting_shader)
ac2 = Entity(model="cube", collider='box', position=(-2.7, -.9, -1.2), scale=(3.2, .7, 1), texture="asset/gray", shader=basic_lighting_shader)

pintu = Entity(model="cube", collider='box', position=(0, -1.79, -1.1), scale=(1, .8, 1), color=color.black, shader=basic_lighting_shader)

mipa = Entity(model="cube", position=(0, 2.5, -2), scale=(1.7, .7, 0), texture="asset/mipa", shader=basic_lighting_shader)
logo_unpak = Entity(model="cube", position=(0, 0.7, -1.2), scale=(1, 1, 1), texture="asset/unpak", shader=basic_lighting_shader)
logo_fmipa = Entity(model="cube", position=(0, -.4, -1.2), scale=.6, texture="asset/log_mipa", shader=basic_lighting_shader)
fmipa = Entity(model="cube", position=(0, -.8, -1.2), scale=(.8, .2, .6), texture="asset/fmipa", shader=basic_lighting_shader)

line1 = Entity(model="cube", collider='box', position=(4.89, 1.5, -2), scale=(.2, 2.97, .2), color=color.white, shader=basic_lighting_shader)
line2 = Entity(model="cube", collider='box', position=(3, 1.5, -2), scale=(.2, 2.97, .2), color=color.white, shader=basic_lighting_shader)
line3 = Entity(model="cube", collider='box', position=(1.11, 1.5, -2), scale=(.2, 2.97, .2), color=color.white, shader=basic_lighting_shader)

line4 = Entity(model="cube", collider='box', position=(-1.11, 1.5, -2), scale=(.2, 2.97, .2), color=color.white, shader=basic_lighting_shader)
line5 = Entity(model="cube", collider='box', position=(-3, 1.5, -2), scale=(.2, 2.97, .2), color=color.white, shader=basic_lighting_shader)
line6 = Entity(model="cube", collider='box', position=(-4.89, 1.5, -2), scale=(.2, 2.97, .2), color=color.white, shader=basic_lighting_shader)

tiang11 = Entity(model="cube", collider='box', position=(4.42, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, 30), color=color.white, shader=basic_lighting_shader)
tiang12 = Entity(model="cube", collider='box', position=(3.47, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, -30), color=color.white, shader=basic_lighting_shader)
penyangga1 = Entity(model="cube", collider='box', position=(3.96, -1.98, -1.85), scale=(.35, .5, .35), rotation=(0, 0, 0), color=color.gray, shader=basic_lighting_shader)

tiang21 = Entity(model="cube", collider='box', position=(2.5, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, 30), color=color.white, shader=basic_lighting_shader)
tiang22 = Entity(model="cube", collider='box', position=(1.55, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, -30), color=color.white, shader=basic_lighting_shader)
penyangga2 = Entity(model="cube", collider='box', position=(2.04, -1.98, -1.85), scale=(.35, .5, .35), rotation=(0, 0, 0), color=color.gray, shader=basic_lighting_shader)

tiang31 = Entity(model="cube", collider='box', position=(-2.5, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, -30), color=color.white, shader=basic_lighting_shader)
tiang32 = Entity(model="cube", collider='box', position=(-1.55, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, 30), color=color.white, shader=basic_lighting_shader)
penyangga3 = Entity(model="cube", collider='box', position=(-2.04, -1.98, -1.85), scale=(.35, .5, .35), rotation=(0, 0, 0), color=color.gray, shader=basic_lighting_shader)

tiang41 = Entity(model="cube", collider='box', position=(-4.42, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, -30), color=color.white, shader=basic_lighting_shader)
tiang42 = Entity(model="cube", collider='box', position=(-3.47, -.89, -1.82), scale=(.1, 2.1, .35), rotation=(0, 0, 30), color=color.white, shader=basic_lighting_shader)
penyangga4 = Entity(model="cube", collider='box', position=(-3.96, -1.98, -1.85), scale=(.35, .5, .35), rotation=(0, 0, 0), color=color.gray, shader=basic_lighting_shader)

bata = Entity(model="cube", collider='box', position=(0, -2.8, 0), scale=(18, 1, 5), color=color.gray, shader=basic_lighting_shader)

ground = Entity(model="plane", collider='box', position=(0, -2.8, -20), scale=50, texture="brick", texture_scale=(50, 50))

orang1 = Animation("asset/right/walk_right",
                   position=(0, -1.8, -1.6), fps=6, loop=True, autoplay=True, scale=(.4, .8, 0))
orang2 = Animation("asset/right/walk_right",
                   position=(3, -1.8, -1.6), fps=6, loop=True, autoplay=True, scale=(.4, .8, 0))
orang3 = Animation("asset/right/walk_right",
                   position=(-2, -1.8, -7), fps=6, loop=True, autoplay=True, scale=(.6, 1, 0))
orang4 = Animation("asset/right/walk_right",
                   position=(-4, -1.8, -7), fps=6, loop=True, autoplay=True, scale=(.6, 1, 0))

# player = Entity(model="cube", position=(0, -1.8, -1.6), scale=(.4, .8, 0), texture="asset/stand/stand_00")
player = Entity(model="cube", position=(-4, -1.8, -7), scale=(.6, 1, 0), texture="asset/stand/stand_00")

def update():
    orang1.x += time.dt * 1
    if orang1.x > 5.5:
        orang1.x = -5.5

    orang2.x += time.dt * 1
    if orang2.x > 5.5:
        orang2.x = -5.5

    orang3.x += time.dt * 1
    if orang3.x > 5:
        orang3.x = -5

    orang4.x += time.dt * 1
    if orang4.x > 5:
        orang4.x = -5

    if held_keys['a']:
        player.texture = None
        player.x -= time.dt * 1
        player.texture = "asset/left/walk_left_00"
    elif held_keys['d']:
        player.texture = None
        player.x += time.dt * 1
        player.texture = "asset/right/walk_right_00"
    else:
        player.texture = "asset/stand/stand_00"
        
    if player.x > 5:
        player.x = -5
    elif player.x < -5:
        player.x = 5

night_light = PointLight(parent=scene, position=(0, 10, -10), color=color.rgba(100, 100, 255, 0.1))

# Sky(texture="asset/malam")

Sky()

app.run()