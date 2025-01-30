from ursina import*

app = Ursina()

from models import*

sky = Sky()
map = Map()
map.new_map(size = 30)

player = Player(speed = 5, jump_height = 3)
window.fullscreen = True

app.run()