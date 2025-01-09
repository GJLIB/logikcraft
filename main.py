from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

sky = sky()
ground = Entity(model = 'plane', scale = 50, collider = 'box', texture = 'grass', texture_scale = (4, 4), position = (0, -2, 0))
block = Entity(model = 'cube', texture = 'grass')
player = FirstPersonController()

app.run()