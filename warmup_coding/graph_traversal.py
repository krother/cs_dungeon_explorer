#
# how is graph traversal different from tree traversal?
# 
import time

maze = """
############
#........###
##.###.#..##
#......##..#
#.##.#..##.#
#.#..#.#...#
#.##.#.###.#
#..#.##..#.#
#..#.......#
############
""".strip().split("\n")

def get_neighbors(x, y):
    yield x - 1, y
    yield x + 1, y
    yield x, y - 1
    yield x, y + 1


start = 1, 1

# lets try to go to all positions by tree traversal
stack = [start]
visited = set()

while len(stack) > 0:
    x, y = stack.pop()  # pop(0) for a QUEUE and level-order traversal
    if (x, y) not in visited:
        print(x, y, end=", ")
        visited.add((x, y))
        for xn, yn in get_neighbors(x, y):
            if maze[yn][xn] == ".":
                stack.append((xn, yn))
