from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y
z = pos.z +1

glowstone = 89
trapdoor = 96
slab = 44
quartz = 155

width = 5
length = 5

# Trapdoor facing direction
south_trap = 4
north_trap = 5
east_trap = 6
west_trap = 7

mc.setBlocks(x, y, z, x+width, y, z+length, quartz)

# South-East Lamp
mc.setBlock(x+1, y, z+1, glowstone)
mc.setBlock(x+1, y+1, z+1, slab)
mc.setBlock(x+1, y, z+2, trapdoor, north_trap)
mc.setBlock(x+2, y, z+1, trapdoor, west_trap)

# Sout-West lamp
mc.setBlock(x+width-1, y, z+1, glowstone)
mc.setBlock(x+width-1, y+1, z+1, slab)
mc.setBlock(x+width-1, y, z+2, trapdoor, north_trap)
mc.setBlock(x+width-2, y, z+1, trapdoor, east_trap)

# North-East Lamp
mc.setBlock(x+1, y, z+length-1, glowstone)
mc.setBlock(x+1, y+1, z+length-1, slab)
mc.setBlock(x+1, y, z+length-2, trapdoor, south_trap)
mc.setBlock(x+2, y, z+length-1, trapdoor, west_trap)

# North-West Lamp
mc.setBlock(x+width-1, y, z+length-1, glowstone)
mc.setBlock(x+width-1, y+1, z+length-1, slab)
mc.setBlock(x+width-1, y, z+length-2, trapdoor, south_trap)
mc.setBlock(x+width-2, y, z+length-1, trapdoor, east_trap)