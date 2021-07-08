from mcpi.minecraft import Minecraft
import mcpi.block as block
mc = Minecraft.create()


pos = mc.player.getTilePos()
x = pos.x +1
y = pos.y
z = pos.z +1
mc.setBlock(x, y, z, block.GLOWING_OBSIDIAN)
