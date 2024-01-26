"""
Code on github.com/krother/cs_dungeon_explorer
"""
import random
from pydantic import BaseModel
from typing import Literal
import logging
import sys

# add logging
log = logging.getLogger()
log.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stderr)
log.addHandler(handler)
fmt = '%(asctime)s | MESSAGE: %(message)s'
handler.setFormatter(logging.Formatter(fmt, datefmt='%m/%d/%Y %I:%M:%S %p'))


logging.info("game logic module is starting")

Command = Literal["left", "right", "up", "down", "jump", "fireball"]

# define the data model
class Position(BaseModel):
    x: int
    y: int


class Player(BaseModel):
    position: Position


class Level(BaseModel):
    structure: list[list[bool]]  # <-- requires Py 3.10 or 3.9


class DungeonObject(BaseModel):
    """Data Exchange Object for the Facade"""
    position: Position
    name: str


class DungeonExplorer(BaseModel):
    player: Player
    level: Level

    def get_objects(self) -> list[DungeonObject]:
        """deliver all parts that need drawing to the graphics engine"""
        result = []
        result.append(DungeonObject(position=self.player.position, name="player"))

        for y, row in enumerate(self.level.structure):
            for x, cell in enumerate(row):
                if cell:
                    result.append(DungeonObject(
                        position=Position(x=x, y=y),
                        name="wall"))
        logging.debug("objects for graphics created")
        return result

    def execute_command(self, cmd: Command) -> None:
        pos = self.player.position
        new_position = pos
        if cmd == "right":
            new_position = Position(x=pos.x + 1, y=pos.y)
        elif cmd == "left":
            new_position = Position(x=pos.x - 1, y=pos.y)
        elif cmd == "up" and pos.y > 0:
            new_position = Position(x=pos.x, y=pos.y -1)
        elif cmd == "down" and pos.y < len(self.level.structure) - 1:
            new_position = Position(x=pos.x, y=pos.y + 1)
        elif cmd == "fireball":
            logging.error("there are no fireballs yet")

        # is there a wall?
        if not self.level.structure[new_position.y][new_position.x]:
            self.player.position = new_position

random.seed(42)
dungeon = DungeonExplorer(
    player = Player(
        position = Position(x=4, y=4)
    ),
    level = Level(
        structure=[
            [random.choice([True, False, False, False, False])
            for x in range(10)]
            for y in range(10)
        ]
    )
)
dungeon.level.structure[4][4] = False


if __name__ == '__main__':
    # code is not executed by tests or other modules importing this
    dungeon.execute_command("right")
    dungeon.execute_command("fireball")
    obj = str(dungeon.get_objects())
    logging.debug(obj)
