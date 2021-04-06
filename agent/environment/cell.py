from enum import Enum, auto


class BattleSnakeCellType(Enum):
    DANGER = auto()
    FOOD = auto()
    EMPTY = auto()


cell_symbols = {
    BattleSnakeCellType.DANGER: "D",
    BattleSnakeCellType.FOOD: "F",
    BattleSnakeCellType.EMPTY: "."
}


class BattleSnakeCell:
    def __init__(self, x, y, type: BattleSnakeCellType):
        self.x = x
        self.y = y
        self.type = type
        self.seen = False # For pathfinding
