
from PIL import Image
import numpy as np


def circle(a, xcenter, ycenter, radius, color):
    Y, X = np.ogrid[0:64, 0:64]
    square_dist = (X - xcenter) ** 2 + (Y - ycenter) ** 2
    mask = square_dist < radius ** 2
    a[mask] = color


a = np.zeros((64, 64, 3), np.uint8)
circle(a, 32, 32, 31, np.array([255, 0, 0], np.uint8))  # red
circle(a, 32, 32, 24, np.array([255, 128, 0], np.uint8))  # orange
circle(a, 32, 32, 16, np.array([255, 255, 0], np.uint8))  # yellow
circle(a, 32, 32, 8, np.array([255, 255, 255], np.uint8))  # white

im = Image.fromarray(a)
im.save('fireball.png')
