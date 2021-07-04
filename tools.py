from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

width = 1
height = 0
length = 1

crafting_table = 58
oak_wood = 17
cobblestone = 4
iron_block = 42
diamond_block = 57
air = 0

mc.setBlocks(x+2 , y, z, x+width, y, z+length, cobblestone)
mc.setBlocks(x+4 , y, z, x+4+width, y, z+length, oak_wood)
mc.setBlocks(x+6 , y, z, x+6+width, y, z+length, iron_block)
mc.setBlocks(x+8 , y, z, x+8+width, y, z+length, diamond_block)
