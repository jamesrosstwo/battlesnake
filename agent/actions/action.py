from enum import Enum, auto


class BattleSnakeAction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    @staticmethod
    def parse_action(action) -> str:
        return action_map[action]


action_map = {
    BattleSnakeAction.UP: "up",
    BattleSnakeAction.DOWN: "down",
    BattleSnakeAction.LEFT: "left",
    BattleSnakeAction.RIGHT: "right",
}



