from mcpi.minecraft import Minecraft

mc = Minecraft.create()


def place_block(x, y, z, id, *state):
    if state:
        mc.setBlock(x, y, z, id, state)
    else:
        mc.setBlock(x, y, z, id)
