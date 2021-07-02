from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def place_block(x, y, z, block, *state):
    if state:
        mc.setBlock(x, y, z, block, state)
    else:
        mc.setBlock(x, y, z, block)

