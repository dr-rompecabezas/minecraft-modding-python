from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y - 1
z = pos.z - 1

ladder = 65
ladder_steps = 30

for step in range(ladder_steps):
    mc.setBlock(x, y, z, ladder)
    y -= 1
