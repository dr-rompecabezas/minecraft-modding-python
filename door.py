from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y
z = pos.z +1

bottom = 0
top = bottom + 8

mc.setBlock(x,y+1,z,block.DOOR_WOOD.id,4)
mc.setBlock(x,y+2,z,block.DOOR_WOOD.id,8)
mc.setBlock(x+1,y+1,z,block.DOOR_WOOD.id,1)
mc.setBlock(x+1,y+2,z,block.DOOR_WOOD.id,8)