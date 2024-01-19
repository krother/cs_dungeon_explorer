"""
Maze Generator

generates a random maze as a string
with '#' being walls and '.' being floors
"""
import random

XMAX, YMAX = 12, 7
PERCOLATION = 5

Position = tuple[int, int]


def create_grid_string(floors: set[Position], xsize: int, ysize: int) -> str:
    """
    Creates a grid of size (xsize, ysize)
    from the given positions of floors.
    """
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            grid += "." if (x, y) in floors else "#"
        grid += "\n"
    return grid


def get_all_floor_positions(xsize: int, ysize: int) -> list[Position]:
    """Returns a list of (x, y) tuples covering all positions in a grid"""
    return [(x, y) for x in range(0, xsize) for y in range(1, ysize - 1)]


def get_neighbors(x: int, y: int) -> list[Position]:
    """Returns a list with the 8 neighbor positions of (x, y)"""
    return [
        (x - 1, y),  # left
        (x + 1, y),  # right
        (x, y - 1),  # up
        (x, y + 1),  # down
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]


def generate_floor_positions(xsize: int, ysize: int) -> set[Position]:
    """
    Creates positions of floors for a random maze

    1. pick a random location in the maze
    2. count how many of its neighbors are already floors
    3. if there are 4 or less, make the position a floor
    4. continue with step 1 until every location has been visited once
    """
    positions = get_all_floor_positions(xsize, ysize)
    floors = set()
    while positions != []:
        x, y = random.choice(positions)
        neighbors = get_neighbors(x, y)
        free = [nb for nb in neighbors if nb in floors]
        if len(free) < PERCOLATION:
            floors.add((x, y))
        positions.remove((x, y))
    return floors


def create_maze(xsize: int, ysize: int) -> str:
    """Returns a xsize*ysize maze as a string"""
    floors = generate_floor_positions(xsize, ysize)
    return create_grid_string(floors, xsize, ysize)


if __name__ == "__main__":
    print(create_maze(32, 20))
