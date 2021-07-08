from mcpi.minecraft import Minecraft
mc = Minecraft.create()

try:
  block = int(input('Block #: '))
except ValueError:
  print('Invalid number entered')
else:
  pos = mc.player.getTilePos()
  x = pos.x +1
  y = pos.y
  z = pos.z +1
  mc.setBlock(x, y, z, block)
