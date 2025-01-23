from ursina import*

app = Ursina()

from models import*



sky = Sky()
map = Map()
map.new_map()



player = Player()

app.run()