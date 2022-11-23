import pandas as pd
import numpy as np
from sys import argv

if len(argv) < 5:
    print('USAGE: python <script> <csv-file-pc> <csv-file-ph> <threshold> <output-file>')
    exit(1)

data = pd.read_csv(argv[1]).to_numpy()
pheromone = pd.read_csv(argv[2]).to_numpy().flatten()
threshold = float(argv[3])
out = argv[4]

cut_data = data[pheromone > (threshold * max(pheromone))]
df = pd.DataFrame(cut_data)
df.to_csv(out, header=False, index=False)
