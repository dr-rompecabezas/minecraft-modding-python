from mcpi.minecraft import Minecraft
mc = Minecraft.create()

try:
  block = int(input('Block #: '))
except ValueError:
  print('Invalid number entered')
else:
  pos = mc.player.getTilePos()
  x = pos.x
  y = pos.y -1
  z = pos.z
  mc.setBlock(x, y, z, block)
