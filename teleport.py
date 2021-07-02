from mcpi.minecraft import Minecraft
mc = Minecraft.create()


def teleport_world_spawn():
    mc.player.setTilePos(0, 0, 0)


def teleport(x, y, z):
    mc.player.setTilePos(x, y, z)


def teleport_precise_pos(x, y, z):
    mc.player.setPos(x, y, z)

teleport_world_spawn()