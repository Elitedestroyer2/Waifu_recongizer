import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import pathlib

data_dir = 'C:\Projects\Waifu_recongizer\Test'

data_dir = pathlib.Path(data_dir)

image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)

character = list(data_dir.glob('kafuu_chino/*'))
t = PIL.Image.open(str(character[0]))
t.show()
PIL.Image.open(str(character[2]))

