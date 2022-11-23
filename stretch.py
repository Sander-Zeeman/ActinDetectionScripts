from PIL import Image
from sys import argv
from skimage.exposure import equalize_adapthist
from skimage import img_as_float, img_as_ubyte

if len(argv) < 3:
    print('USAGE: python <script> <image> <output-file>')
    exit(1)

filename = argv[1]
out = argv[2]

img = Image.open(filename)
img = equalize_adapthist(img_as_float(img))
img = img_as_ubyte(img)
img = Image.fromarray(img)
img.save(out)
