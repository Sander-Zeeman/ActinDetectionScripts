import pandas as pd
from sys import argv

if len(argv) < 5:
    print('USAGE: python <script> <csv-file> <width> <height> <output-file>')
    exit(1)

data = pd.read_csv(argv[1]).to_numpy()
width = int(argv[2])
height = int(argv[3])
out = argv[4]

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

print(f'({x_low}, {y_low}) - ({x_high}, {y_high})')

booleans = []
for point in data:
    booleans.append(point[0] >= x_low and point[0] <=
                    x_high and point[1] >= y_low and point[1] <= y_high)

cut_data = data[booleans]
df = pd.DataFrame(cut_data)
df.to_csv(out, header=False, index=False)
