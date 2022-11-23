from PIL import Image
from skimage.filters import frangi
from skimage import img_as_ubyte
import numpy as np
from skimage.exposure import equalize_hist, rescale_intensity
from sys import argv

if len(argv) < 3:
    print('USAGE: python <script> <image>')
    exit(1)


filename = argv[1]
out = argv[2]

image = np.array(Image.open(filename))
image = equalize_hist(image)
frangi_img = frangi(image, sigmas=range(3, 6, 1), gamma=50, black_ridges=False)
frangi_img = rescale_intensity(frangi_img)
show_image = Image.fromarray(img_as_ubyte(frangi_img))
show_image.save(out)
