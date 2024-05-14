from random import randint
from sty import fg
def generate_rgb () -> list[int, int, int]:
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return [red, green, blue]

def generate_fg_color(red:int, green:int, blue:int):
    return fg(red, green, blue)

rgb = generate_rgb()
print(generate_fg_color(rgb[0], rgb[1], rgb[2]), 'Hello World!')