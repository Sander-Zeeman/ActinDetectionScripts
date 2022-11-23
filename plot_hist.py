import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

if len(argv) < 4:
    print('USAGE: python <script> <csv-file> <width> <height> <output-file (empty if show)> ')
    exit(1)

data = pd.read_csv(argv[1]).to_numpy().T
width = int(argv[2])
height = int(argv[3])
out = argv[4] if len(argv) == 5 else ""

plt.hist2d(data[0], data[1], bins=[width, height], cmap='turbo')

plt.margins(0, 0)
plt.gca().invert_yaxis()
plt.gca().set_axis_off()
plt.gca().set_aspect('equal')

plt.xlim(0, width)
plt.ylim(height, 0)
plt.tight_layout()

if out == "":
    plt.show()
else:
    plt.savefig(out, bbox_inches='tight', pad_inches=0)
