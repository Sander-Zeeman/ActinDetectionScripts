import pandas as pd
import matplotlib.pyplot as plt
from sys import argv

if len(argv) < 4:
    print('USAGE: python <script> <csv-file> <top-left coords: (x,y)> <bottom-left coords: (x,y)> <output-file (empty if show)>')
    exit(1)

data = pd.read_csv(argv[1]).to_numpy().T
top_left = [int(d) for d in argv[2].strip().split(',')]
bottom_right = [int(d) for d in argv[3].strip().split(',')]
out = argv[4] if len(argv) == 5 else ""


plt.scatter(data[0], data[1], c='blue', s=0.01)

plt.margins(0, 0)
plt.gca().invert_yaxis()
plt.gca().set_axis_off()
plt.gca().set_aspect('equal')

plt.xlim(top_left[0], bottom_right[0])
plt.ylim(bottom_right[1], top_left[1])
plt.tight_layout()
if out == "":
    plt.show()
else:
    plt.savefig(out, bbox_inches='tight', pad_inches=0)
