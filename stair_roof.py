from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y
z = pos.z +1

stair = block.STAIRS_WOOD.id
# torch = block.TORCH.id
east = 0
west = 1
south = 2
north = 3

width = 5
length = 5

mc.setBlocks(x, y, z+1, x, y, z+length, stair, east)
mc.setBlocks(x+width, y, z+1, x+width, y, z+length, stair, west)
mc.setBlocks(x+1, y, z+length, x+width-1, y, z+length, stair, north)
mc.setBlocks(x+1, y, z+1, x+width-1, y, z+1, stair, south)

# mc.setBlocks(x, y+1, z+1, x, y+1, z+length, torch, east)
# mc.setBlocks(x+width, y+1, z+1, x+width, y+1, z+length, torch, west)
# mc.setBlocks(x+1, y+1, z+length, x+width-1, y+1, z+length, torch, north)
# mc.setBlocks(x+1, y+1, z+1, x+width-1, y+1, z+1, torch, south)
