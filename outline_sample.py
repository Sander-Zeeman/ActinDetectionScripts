from PIL import Image, ImageDraw
from sys import argv

if len(argv) < 3:
    print('USAGE: python <script> <image> <output-file>')
    exit(1)

filename = argv[1]
out = argv[2]

# Measured relative to one another
top_left = (157, 152)
full_size = (758, 758)
sample_size = (208, 208)

img = Image.open(filename)
actual_size = img.size
x_ratio = actual_size[1] / full_size[1]
y_ratio = actual_size[0] / full_size[0]

y_low = int(top_left[0]*y_ratio)
y_high = int((top_left[0] + sample_size[0]) * y_ratio)
x_low = int(top_left[1]*x_ratio)
x_high = int((top_left[1]+sample_size[1])*x_ratio)

draw = ImageDraw.Draw(img)
draw.rectangle([x_low, y_low, x_high, y_high], width=3, outline="#FFFFFF")
img.save(out)
