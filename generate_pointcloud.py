from PIL import Image
import numpy as np
import pandas as pd
from sys import argv

if len(argv) < 4:
    print('USAGE: python <script> <image> <scale> <output-file>')
    exit(1)

filename = argv[1]
scale = float(argv[2])
out = argv[3]

data = np.array(Image.open(filename))
data = data.astype('float')
data = np.floor(data * scale)
data = data.astype('uint8')

pc = np.empty((0, 3), float)
for y, row in enumerate(data):
    print(f'Generated points for row {y}/{len(data)}')
    for x, val in enumerate(row):
        randoms = np.random.rand(val, 2)
        zeros = np.zeros((val, 1))
        local_points = np.concatenate((randoms, zeros), axis=1)
        pc = np.concatenate((pc, local_points + [x, y, 0]), axis=0)

df = pd.DataFrame(pc)
df.to_csv(out, header=False, index=False)
