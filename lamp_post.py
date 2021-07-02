from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def create_lamp_post(x, y, z):
    fence = 85
    glowstone = 89
    trapdoor = 96
    slab = 44
    mc.setBlock(x, y, z, fence)
    mc.setBlock(x, y+1, z, fence)
    mc.setBlock(x, y+2, z, fence)
    mc.setBlock(x, y+3, z, glowstone)
    mc.setBlock(x, y+3, z-1, trapdoor, 4)
    mc.setBlock(x, y+3, z+1, trapdoor, 5)
    mc.setBlock(x-1, y+3, z, trapdoor, 6)
    mc.setBlock(x+1, y+3, z, trapdoor, 7)
    mc.setBlock(x, y+4, z, slab)

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

create_lamp_post(x, y, z)