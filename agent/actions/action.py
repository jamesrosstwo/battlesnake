from enum import Enum, auto


class BattleSnakeAction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


action_map = {
    BattleSnakeAction.UP: "up",
    BattleSnakeAction.DOWN: "down",
    BattleSnakeAction.LEFT: "left",
    BattleSnakeAction.RIGHT: "right",
}


def parse_action(action: BattleSnakeAction) -> str:
    return action_map[action]
