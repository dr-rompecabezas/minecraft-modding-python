from mcpi.block import Block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = input('Enter block id number: ')

pos = mc.player.getTilePos()
x = pos.x

