from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

width = 8
height = 4
length = 6

crafting_table = 58
oak_wood = 17
cobblestone = 4
iron_block = 42
diamond_block = 57
quartz = 155
air = 0

mc.setBlocks(x, y, z, x+width, y+height, z+length, quartz)
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+length-1, air)