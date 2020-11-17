"""
CTRL-C / CTRL-V + Bugs

https://softwareengineering.stackexchange.com/questions/159830/nearest-color-algorithm-using-hex-triplet
https://stackoverflow.com/questions/3241929/python-find-dominant-most-common-color-in-an-image
https://stackoverflow.com/questions/3380726/converting-a-rgb-color-tuple-to-a-six-digit-code-in-python

"""
from PIL import Image, ImageColor
import math
import colornames


# Define file path
FILEPATH = "/tmp/a.png"

def compute_average_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x, y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    return (r_total / count, g_total / count, b_total / count)


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

img = Image.open(FILEPATH)
img = img.convert('RGB')
average_color = compute_average_image_color(img)
average_color_int = tuple([int(i) for i in average_color])

hexcolor = rgb_to_hex(average_color_int)
selected_color_hex = None
selected_color_name = None
selected_distance = 999999

for color_hex, color_name in colornames.colornames.items():
    color_rgb = ImageColor.getrgb(color_hex)
    try:
        distance = math.sqrt(average_color_int[0] - color_rgb[0]) + \
                   math.sqrt(average_color_int[1] - color_rgb[1]) + \
                   math.sqrt(average_color_int[2] - color_rgb[2])
    except ValueError:
        continue

    if distance < selected_distance:
        selected_color_hex = color_hex
        selected_color_name = color_name


print("Avarage Color Original: " + hexcolor)
if selected_color_hex:
    print("Average Color Approximate: {} - {}".format(selected_color_hex, selected_color_name))
else:
    print("Color not found")
