from enum import Enum, auto


class BattleSnakeAction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    @staticmethod
    def parse_action(action) -> str:
        return _action_map[action]


_action_map = {
    BattleSnakeAction.UP: "up",
    BattleSnakeAction.DOWN: "down",
    BattleSnakeAction.LEFT: "left",
    BattleSnakeAction.RIGHT: "right",
}
