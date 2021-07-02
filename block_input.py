from mcpi.block import Block
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = int(input('Enter block id number:  '))

pos = mc.player.getTilePos()
x = pos.x 
y = pos.y
z = pos.z 

mc.setBlock(x, y-1, z, block)

print("block: ", block)
