"""
Requirement: walls that stop the player.

Code on github.com/krother/cs_dungeon_explorer
"""
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

# TODO: handle file not found situation
wall = double_size(cv2.imread("tiles/wall.png"))

def draw(player, level):
    """draws the player image on the screen"""
    frame = np.zeros((SCREEN_SIZE_X, SCREEN_SIZE_Y, 3), dtype=np.uint8)
    # draw the player
    xpos, ypos = player.position.x * TILE_SIZE, player.position.y * TILE_SIZE
    if 0 <= xpos <= X_BOUNDARY and 0 <= ypos <= Y_BOUNDARY:
        frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = player.image

    for y, row in enumerate(level.structure):
        for x, cell in enumerate(row):
            if cell:
                xpos, ypos = x * TILE_SIZE, y * TILE_SIZE
                if 0 <= xpos <= X_BOUNDARY and 0 <= ypos <= Y_BOUNDARY:
                    frame[ypos : ypos + TILE_SIZE, xpos : xpos + TILE_SIZE] = wall

    cv2.imshow("frame", frame)



player = Player(
    image = double_size(cv2.imread("tiles/deep_elf_high_priest.png")),
    position = Position(x=4, y=4)
)
level = Level(
    structure=[
        [random.choice([True, False, False, False, False])
         for x in range(10)]
        for y in range(10)
    ]
)
level.structure[4][4] = False


exit_pressed = False

while not exit_pressed:
    draw(player, level)

    # handle keyboard input
    key = chr(cv2.waitKey(1) & 0xFF)
    new_position = player.position
    if key == "d":
        new_position = Position(x=player.position.x + 1, y=player.position.y)
    elif key == "a":
        new_position = Position(x=player.position.x - 1, y=player.position.y)
    elif key == "w" and player.position.y > 0:
        new_position = Position(x=player.position.x, y=player.position.y -1)
    elif key == "s" and player.position.y < LEVEL_SIZE_Y - 1:
        new_position = Position(x=player.position.x, y=player.position.y + 1)
    elif key == "q":
        exit_pressed = True

    # is there a wall?
    if not level.structure[new_position.y][new_position.x]:
        player.position = new_position

cv2.destroyAllWindows()



