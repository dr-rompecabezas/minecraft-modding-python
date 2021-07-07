from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()

# Set minimum value of 5 for width and length 
# to make room for interior lamps
width = 7
height = 4
length = 7

# Global position variables
pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y -1
z = pos.z +1

# Blocks for walls, floor and interior
quartz = 155
air = 0

# Walls and floor
mc.setBlocks(x, y, z, x+width, y+height, z+length, quartz)

# House interior (empty space) within the walls plus roof opening
mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height, z+length-1, air)

# Blocks for roof
stair = block.STAIRS_WOOD.id
east = 0
west = 1
south = 2
north = 3
rooftop = block.WOOD_PLANKS.id

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
    rooftop)

# Interior Design
# Interior lamps

# Blocks for lamps
glowstone = 89
trapdoor = 96
slab = 44
quartz = 155

# Trapdoor facing direction
south_trap = 4
north_trap = 5
east_trap = 6
west_trap = 7

# Offset height for floor level
floor = y +1

# South-East Lamp
mc.setBlock(x+1, floor, z+1, glowstone)
mc.setBlock(x+1, floor+1, z+1, slab)
mc.setBlock(x+1, floor, z+2, trapdoor, north_trap)
mc.setBlock(x+2, floor, z+1, trapdoor, west_trap)

# Sout-West lamp
mc.setBlock(x+width-1, floor, z+1, glowstone)
mc.setBlock(x+width-1, floor+1, z+1, slab)
mc.setBlock(x+width-1, floor, z+2, trapdoor, north_trap)
mc.setBlock(x+width-2, floor, z+1, trapdoor, east_trap)

# North-East Lamp
mc.setBlock(x+1, floor, z+length-1, glowstone)
mc.setBlock(x+1, floor+1, z+length-1, slab)
mc.setBlock(x+1, floor, z+length-2, trapdoor, south_trap)
mc.setBlock(x+2, floor, z+length-1, trapdoor, west_trap)

# North-West Lamp
mc.setBlock(x+width-1, floor, z+length-1, glowstone)
mc.setBlock(x+width-1, floor+1, z+length-1, slab)
mc.setBlock(x+width-1, floor, z+length-2, trapdoor, south_trap)
mc.setBlock(x+width-2, floor, z+length-1, trapdoor, east_trap)

# Door Gap (East facing)
mc.setBlocks(
    x, floor, z+2,
    x, floor+1, z+3, 
    air)

# Windows (West, South and North facing)
glass = 95

# South windows
mc.setBlocks(
    x+2, floor+1, z, 
    x+width-2, floor+height-2, z, 
    glass)

# North windows
mc.setBlocks(
    x+2, floor+1, z+length, 
    x+width-2, floor+height-2, z+length, 
    glass)

# West windows
mc.setBlocks(
    x+width, floor+1, z+2,
    x+width, floor+height-2, z+length-2, 
    glass)