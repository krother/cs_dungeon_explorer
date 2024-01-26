"""
Requirement: walls that stop the player.

Code on github.com/krother/cs_dungeon_explorer
"""
from game_logic import dungeon
import numpy as np
import cv2


LEVEL_SIZE_X, LEVEL_SIZE_Y = 10, 10
TILE_SIZE = 64  # measured in pixel

SCREEN_SIZE_X, SCREEN_SIZE_Y = LEVEL_SIZE_X * TILE_SIZE, LEVEL_SIZE_Y * TILE_SIZE  # tuple
X_BOUNDARY = SCREEN_SIZE_X - TILE_SIZE
Y_BOUNDARY = SCREEN_SIZE_Y - TILE_SIZE



def double_size(img):
    """returns an image twice as big"""
    return np.kron(img, np.ones((2, 2, 1), dtype=img.dtype))

IMAGES = {
    "player": double_size(cv2.imread("tiles/deep_elf_high_priest.png")),
    "wall": double_size(cv2.imread("tiles/wall.png")),
}

def draw(dungeon):
    """draws the player image on the screen"""
    frame = np.zeros((SCREEN_SIZE_X, SCREEN_SIZE_Y, 3), dtype=np.uint8)
    for obj in dungeon.get_objects():
        img = IMAGES[obj.name]
        xpos, ypos = obj.position.x * TILE_SIZE, obj.position.y * TILE_SIZE
        if 0 <= xpos <= X_BOUNDARY and 0 <= ypos <= Y_BOUNDARY:
            frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = img

    cv2.imshow("frame", frame)



MOVES = {
    "d": "right",
    "a": "left",
    "w": "up",
    "s": "down",
}
exit_pressed = False
while not exit_pressed:
    draw(dungeon)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    cmd = MOVES.get(key)
    if cmd:
        dungeon.execute_command(cmd)
    elif key == "q":
        exit_pressed = True

cv2.destroyAllWindows()



