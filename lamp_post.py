import set_blocks as sb


def create_lamp_post(x, z):
    x = 8
    z = 5
    fence = 85
    glow_stone = 89
    trapdoor = 96
    sb.place_block(x, 1, z, fence)
    sb.place_block(x, 2, z, fence)
    sb.place_block(x, 3, z, fence)
    sb.place_block(x, 4, z, glow_stone)
    sb.place_block(x, 4, z-1, trapdoor, 4)
    sb.place_block(x-1, 4, z, trapdoor, 6)
    sb.place_block(x+1, 4, z, trapdoor, 7)
    sb.place_block(x, 4, z+1, trapdoor, 5)
