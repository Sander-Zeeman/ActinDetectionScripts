import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize
from sys import argv

if len(argv) < 6:
    print('USAGE: python <script> <csv-file-pc> <csv-file-ph> <top-left coords: (x,y)> <bottom-left coords: (x,y)> <threshold> <output-file (empty if show)>')
    exit(1)

data = pd.read_csv(argv[1]).to_numpy().T
pheromone = pd.read_csv(argv[2]).to_numpy().flatten()
top_left = [int(d) for d in argv[3].strip().split(',')]
bottom_right = [int(d) for d in argv[4].strip().split(',')]
threshold = float(argv[5])
out = argv[6] if len(argv) == 7 else ""

normalizer = Normalize(vmin=0, vmax=max(pheromone))
pheromone = normalizer(pheromone)

data = data[:, pheromone > threshold]
pheromone = pheromone[pheromone > threshold]
colors = cm.turbo(pheromone)

plt.scatter(data[0], data[1], c=colors, s=0.01)

plt.margins(0, 0)
plt.gca().invert_yaxis()
plt.gca().set_axis_off()
plt.gca().set_aspect('equal')

plt.xlim(top_left[0], bottom_right[0])
plt.ylim(bottom_right[1], top_left[1])
plt.colorbar(cm.ScalarMappable(cmap='turbo'))
plt.tight_layout()

if out == "":
    plt.show()
else:
    plt.savefig(out, bbox_inches='tight', pad_inches=0)
