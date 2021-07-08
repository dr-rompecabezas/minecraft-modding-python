from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Keep length and width fixed at 6
# For table to be one block away from bookshelves
width = 6
height = 3
length = 6

# Global position variables
pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y -1
z = pos.z +1

# Offset height for floor level
floor = y +1

mc.postToChat(f"Enchantment house built at coords: {x},{y},{z}")

# Blocks for walls, floor and interior
stone_bricks = 98
air = 0

# Walls and floor
mc.setBlocks(x, y, z, x+width, y+height, z+length, stone_bricks)

# House interior (empty space) within the walls plus roof opening
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height, z+length-1, air)

# Bookshelves
bookshelf = 47
# South wall bookshelves
mc.setBlocks(
    x+2, floor, z+1, 
    x+width-1, floor+1, z+1, 
    bookshelf)
# North wall bookshelves
mc.setBlocks(
    x+2, floor, z+length-1, 
    x+width-1, floor+1, z+length-1, 
    bookshelf)
# East wall bookshelves
mc.setBlocks(
    x+width-1, floor, z+2, 
    x+width-1, floor+1, z+length-2, 
    bookshelf)

# Enchantment table
enchantment_table = 116
mc.setBlock(x+((width/2)+0.5), floor, z+(length/2), enchantment_table)

# Lamps
glowstone = 89
mc.setBlock(x+1, floor, z+1, glowstone)
mc.setBlock(x+1, floor, z+length-1, glowstone)

# Chests
chest = 54
mc.setBlock(x+2, floor+1, z+1, chest, 3)
mc.setBlock(x+2, floor+1, z+length-1, chest, 2)

# Roof
# Blocks for roof
stair = 53
east = 0
west = 1
south = 2
north = 3
oak_log = 17

# Offset height for roof base
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

# Roof Level 2 (Base + 1)
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

# Roof Level 3 (Base + 2)
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

# Rooftop (Base + 2)
mc.setBlocks(
    x+2, roof_base+2, z+2, 
    x+width-2, roof_base+2, z+length-2, 
    oak_log)


# Door (West side)
# If doors do not work in your Minecraft version, 
# collect the door and place it manually
door = 64
mc.setBlock(x, floor, z+(length/2), door, 4)
mc.setBlock(x, floor+1, z+(length/2), door, 8)
