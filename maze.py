from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create()

gap = block.AIR.id
wall = block.STONE_BRICK.id
floor = block.BEDROCK.id

filename = "csv_files/mc_maze.csv"
with open(filename) as file:
    data = file.readlines()

pos = mc.player.getTilePos()
origin_x = pos.x + 1
y = pos.y
z = pos.z + 1

for line in data:
    maze = line.split(",")
    x = origin_x
    for cell in maze:
        if cell == "0":
            b = gap
        else:
            b = wall
        mc.setBlock(x, y, z, b)
        mc.setBlock(x, y+1, z, b)
        mc.setBlock(x, y-1, z, floor)
        x += 1
    z += 1
