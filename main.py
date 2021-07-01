import teleport as tp
import set_blocks as sb
import lamp_post as lp

# Pass x, y, z coordinates as integers
# Found a ship wreck at (200, 120, -600)
# tp.teleport(200, 120, -600)

# Teleport to original spawn point (0, 0, 0)
# tp.teleport_world_spawn()

# Teleport to a precise location on a block
# # Pass x, y, z coordinates as integers or floats
# tp.teleport_precise_pos()

# for y in range(0, 20):
#     sb.place_block(0, y, 2, 65)

# Bridge Builder

# for i in range(25):
#     sb.place_block(x, 0, z, 17)
#     x += 1
#     z += 1

# counter = -17
# for i in range(30):
#     sb.place_block(0, 0, counter, 50)
#     counter -= 1


def give_me_cake():
    sb.place_block(-3, 0, 0, 92)


# give_me_cake()


def get_me_to_top():
    tp.teleport(1, 22, 1)


# get_me_to_top()


