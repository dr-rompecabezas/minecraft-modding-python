from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

blocks = [155, 41, 169, 98]
parkour_distance = 8

def parkour_gen():
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y -1
    z = pos.z
    for i in range(parkour_distance):
        random_x = random.randint(0, 2)
        random_y = random.randint(-1, 1)
        random_z = random.randint(0, 2)
        mc.setBlock(x, y, z, random.choice(blocks))
        x += random_x
        y += random_y
        z -= random_z

parkour_gen()