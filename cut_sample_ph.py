import pandas as pd
from sys import argv

if len(argv) < 5:
    print('USAGE: python <script> <csv-file-pc> <csv-file-ph> <width> <height> <output-file>')
    exit(1)

data = pd.read_csv(argv[1]).to_numpy()
pheromone = pd.read_csv(argv[2]).to_numpy().flatten()
width = int(argv[3])
height = int(argv[4])
out = argv[5]

top_left = (157, 152)
full_size = (758, 758)
sample_size = (208, 208)

actual_size = (width, height)
x_ratio = actual_size[1] / full_size[1]
y_ratio = actual_size[0] / full_size[0]

y_low = int(top_left[0]*y_ratio)
y_high = int((top_left[0] + sample_size[0]) * y_ratio)
x_low = int(top_left[1]*x_ratio)
x_high = int((top_left[1]+sample_size[1])*x_ratio)

booleans = []
for point in data:
    booleans.append(point[0] >= x_low and point[0] <=
                    x_high and point[1] >= y_low and point[1] <= y_high)

cut_data = pheromone[booleans]
df = pd.DataFrame(cut_data)
df.to_csv(out, header=False, index=False)
