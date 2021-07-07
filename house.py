from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()

# crafting_table = 58
# oak_wood = 17
# cobblestone = 4
# iron_block = 42
# diamond_block = 57
quartz = 155
air = 0

stair = block.STAIRS_WOOD.id
east = 0
west = 1
south = 2
north = 3

pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y
z = pos.z +1

width = 6
height = 4
length = 8

# walls and floor
mc.setBlocks(x, y, z, x+width, y+height, z+length, quartz)

# empty space inside the house and roof opening
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height, z+length-1, air)

roof_base = y+height+1

# Roof Base
# East and West facing stairs run along the z coordinate
mc.setBlocks(
    x-1, roof_base, z-1, 
    x-1, roof_base, z+length+1, 
    stair, east)
mc.setBlocks(
    x+width+1, roof_base, z-1, 
    x+width+1, roof_base, z+length+1, 
    stair, west)
# North and South facing stairs run along the x coordinate
mc.setBlocks(
    x, roof_base, z+length+1, 
    x+width, roof_base, z+length+1, 
    stair, north)
mc.setBlocks(
    x, roof_base, z-1, 
    x+width, roof_base, z-1, 
    stair, south)

# Roof Base + 1
# East and West facing stairs run along the z coordinate
mc.setBlocks(
    x, roof_base+1, z, 
    x, roof_base+1, z+length, 
    stair, east)
mc.setBlocks(
    x+width, roof_base+1, z, 
    x+width, roof_base+1, z+length, 
    stair, west)
# North and South facing stairs run along the x coordinate
mc.setBlocks(
    x+1, roof_base+1, z+length, 
    x+width-1, roof_base+1, z+length, 
    stair, north)
mc.setBlocks(
    x+1, roof_base+1, z, 
    x+width-1, roof_base+1, z, 
    stair, south)

# Roof Base + 2
# East and West facing stairs run along the z coordinate
mc.setBlocks(
    x+1, roof_base+2, z+1, 
    x+1, roof_base+2, z+length-1, 
    stair, east)
mc.setBlocks(
    x+width-1, roof_base+2, z+1, 
    x+width-1, roof_base+2, z+length-1, 
    stair, west)
# North and South facing stairs run along the x coordinate
mc.setBlocks(
    x+2, roof_base+2, z+length-1, 
    x+width-2, roof_base+2, z+length-1, 
    stair, north)
mc.setBlocks(
    x+2, roof_base+2, z+1, 
    x+width-2, roof_base+2, z+1, 
    stair, south)

# Rooftop
mc.setBlocks(
    x+2, roof_base+2, z+2, 
    x+width-2, roof_base+2, z+length-2, 
    block.WOOD_PLANKS.id)