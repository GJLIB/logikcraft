from ursina import *
from perlin_noise import PerlinNoise
from ursina.shaders import basic_lighting_shader
from numpy import floor
import os
from ursina.prefabs.first_person_controller import FirstPersonController

block_textures = []
BASE_DIR = os.getcwd()
BLOCKS_DIR = os.path.join(BASE_DIR, 'assets/blocks')
file_list = os.listdir(BLOCKS_DIR)

for image in file_list:
    texture = load_texture('assets/blocks' + os.sep + image)
    block_textures.append(texture)



class Block(Entity):
    def __init__(self, block_type, pos, **kwargs):
        super().__init__(
            parent = scene, 
            model = 'cube',
            texture = block_textures[block_type],
            position = pos,
            scale = 1,
            collider = 'box',
            origin_y = -0.5,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            shader = basic_lighting_shader,
            **kwargs
        )

class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, collider=None, **kwargs)
        self.bedrock = Entity(model='plane', collider='box', scale=100, texture='grass', texture_scale=(4,4), position=(0,-2,0))
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=2500)

    def new_map(self, size = 30):
        for x in range(size):
            for z in range(size):
                y = floor(self.noise([x/24, z/24])*6)
                block = Block(4, (x, y, z))

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def input(self, key):
        super().input(key)
        if key == 'left mouse down' and mouse.hovered_entity:
            destroy(mouse.hovered_entity)
        if key == 'right mouse down' and mouse.hovered_entity:
            hit_info = raycast(camera.world_position, camera.forward, distance = 15)
            if hit_info.hit:
                Block(1, hit_info.entity.position + hit_info.normal)