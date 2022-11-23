from PIL import Image
import numpy as np

from os import mkdir, path
from sys import exit


def validity_checks_init():
    if not path.isdir('./data'):
        print('No data/ folder found in the current directory.')
        exit(1)

    if path.isdir('./prepared_data'):
        print('Please remove the existing prepared_data/ folder.')
        exit(1)

    if not path.isfile('./data/desc.txt'):
        print('No data description \'desc.txt\' found in the data folder.')
        exit(1)


def validity_checks_desc(descriptions):
    for desc in descriptions:
        if not path.isfile(f'./data/{desc[0]}_sted.tif') or not path.isfile(f'./data/{desc[0]}_conf.tif'):
            print(
                f'File ./data/{desc[0]}_sted.tif or ./data/{desc[0]}_conf.tif does not exist.')
            exit(1)


def normalize_image(data):
    data -= data.min()
    data = data.astype('float32')
    data *= (255 / data.max())
    return data.astype('uint8')


def process_file(file, desc):
    [x, y, w, h, out] = desc

    # Load image
    img = Image.open(file)

    # Normalize image
    data = normalize_image(np.array(img))

    # Cut image
    if not (w == 0 or h == 0):
        data = data[x:x+w, y:y+h]

    # Write image
    Image.fromarray(data).save(f'./prepared_data/{out}_{file[-8:-4]}.bmp')


def process_description(desc):
    [num, x, y, w, h, out] = desc
    process_file(f'./data/{num}_conf.tif', desc[1:])
    process_file(f'./data/{num}_sted.tif', desc[1:])


if __name__ == '__main__':
    validity_checks_init()

    with open('./data/desc.txt', 'r') as f:
        descriptions_str = ''.join(f.readlines()).split('\n')
        descriptions = [
            [
                int(string)
                if string.isnumeric() else string
                for string in desc_str.split(' ')
            ]
            for desc_str in descriptions_str
        ]

        validity_checks_desc(descriptions)
        mkdir('./prepared_data')

        for desc in descriptions:
            process_description(desc)
