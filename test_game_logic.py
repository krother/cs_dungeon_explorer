
from game_logic import DungeonExplorer, DungeonObject, Player, Level, Position
import pytest

def test_add():
    # 1. define test data
    a, b = 3, 4
    # 2. execute the code under test
    result = sum([a, b])
    # 3. check whether the result is what you expect
    assert result == 7


@pytest.fixture
def empty_dungeon():
    """an 3x3 dungeon without walls"""
    return DungeonExplorer(
        player=Player(position=Position(x=1, y=1)),
        level=Level(structure=[[False, False, False], [False, False, False], [False, False, False]])
    )

MOVES = [
    ("right", 2, 1),
    ("left", 0, 1),
    ("up", 1, 0),
    ("down", 1, 2),
]

@pytest.mark.parametrize("direction, x, y", MOVES)
def test_move(empty_dungeon, direction, x, y):
    """the player can move to the right"""
    empty_dungeon.execute_command(direction)
    assert DungeonObject(
        position=Position(x=x, y=y), 
        name="player"
    ) in empty_dungeon.get_objects()

@pytest.mark.parametrize("direction, x, y", MOVES)
def test_move_into_wall(empty_dungeon, direction, x, y):
    """the player cannot move if there is a wall"""
    empty_dungeon.level.structure[y][x] = True
    empty_dungeon.execute_command(direction)
    assert DungeonObject(
        position=Position(x=1, y=1),
        name="player"
        ) in empty_dungeon.get_objects()
