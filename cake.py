from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x + 1
y = pos.y
z = pos.z

cake = 92
mc.setBlock(x, y, z, cake)
mc.postToChat(f"Cake ready to eat at coords: {x},{y},{z}")
