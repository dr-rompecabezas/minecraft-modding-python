from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def create_inside_light(x, y, z):
 
    glowstone = 89
    trapdoor = 96
    slab = 44
 
    mc.setBlock(x, y, z, glowstone)
    # mc.setBlock(x, y, z-1, trapdoor, 4)
    mc.setBlock(x, y, z+1, trapdoor, 5)
    mc.setBlock(x-1, y, z, trapdoor, 6)
    # mc.setBlock(x+1, y, z, trapdoor, 7)
    mc.setBlock(x, y+1, z, slab)

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

create_inside_light(x, y, z)