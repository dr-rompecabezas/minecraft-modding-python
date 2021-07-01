from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()


def teleport_world_spawn():
    time.sleep(1)
    mc.player.setTilePos(0, 0, 0)


def teleport(x, y, z):
    # time.sleep(10)
    mc.player.setTilePos(x, y, z)


def teleport_precise_pos(x, y, z):
    time.sleep(10)
    mc.player.setPos(x, y, z)
