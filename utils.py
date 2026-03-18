import numpy as np


def pixel_generator(image):
    for row in image:
        yield row