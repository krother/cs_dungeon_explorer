"""
Proof-of-concept: move around on a 2D grid

Install dependencies:

    pip install opencv-python
"""
import numpy as np
import cv2


LEVEL_SIZE_X, LEVEL_SIZE_Y = 10, 10

TILE_SIZE = 64  # measured in pixel

SCREEN_SIZE_X, SCREEN_SIZE_Y = LEVEL_SIZE_X * TILE_SIZE, LEVEL_SIZE_Y * TILE_SIZE  # tuple
X_BOUNDARY = SCREEN_SIZE_X - TILE_SIZE
Y_BOUNDARY = SCREEN_SIZE_Y - TILE_SIZE



def draw_player(background, player, x, y):
    """draws the player image on the screen"""
    frame = background.copy()
    xpos, ypos = x * TILE_SIZE, y * TILE_SIZE
    if 0 <= xpos <= X_BOUNDARY and 0 <= ypos <= Y_BOUNDARY:
        frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = player
    cv2.imshow("frame", frame)


def double_size(img):
    """returns an image twice as big"""
    return np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))


# load image
player = double_size(cv2.imread("tiles/deep_elf_high_priest.png"))
# TODO: do something about imread returning None values

# create black background image with BGR color channels
background = np.zeros((SCREEN_SIZE_Y, SCREEN_SIZE_X, 3), np.uint8)

# starting position of the player in dungeon
x, y = 4, 4

exit_pressed = False

while not exit_pressed:
    draw_player(background, player, x, y)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == "d":
        x += 1
    elif key == "a":
        x -= 1
    elif key == "w" and y > 0:
        y -= 1
    elif key == "s" and y < LEVEL_SIZE_Y - 1:
        y += 1
    elif key == "q":
        exit_pressed = True

cv2.destroyAllWindows()



