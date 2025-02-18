import random

COLORS = [(237, 128, 128), (228, 128, 237), (125, 82, 242), (47, 46, 92), (137, 159, 214), (126, 197, 247),
          (72, 111, 120), (68, 252, 231), (130, 232, 190), (113, 222, 144), (111, 191, 119), (158, 252, 134),
          (252, 226, 96), (252, 174, 157), (220, 127, 235), (161, 160, 232)]


def different_colors_():
    color_index = random.randint(0, 15)
    if color_index == 16:
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    else:
        return COLORS[color_index]
