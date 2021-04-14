from agent.environment.board import BattleSnakeBoard, BoardCoord
from agent.state_machine import BattleSnakeStateMachine
from agent.actions.action import BattleSnakeAction
from agent.states.state_food import BattleSnakeFoodState


class BattleSnakeAgent:
    def __init__(self):
        self.state_machine = BattleSnakeStateMachine(self)
        self.board = None
        self.pos = None

    def select_state(self, board) -> "BattleSnakeState":
        pass

    def parse_board(self, board):
        pass

    def act(self, board_json) -> "BattleSnakeAction":
        self.board = BattleSnakeBoard(board_json)
        self.pos = BoardCoord(board_json["you"]["head"]["x"], board_json["you"]["head"]["y"])
        print("start: ", self.pos)
        self.state_machine.change_state(BattleSnakeFoodState.instance())
        return self.state_machine.calculate_action()


from agent.states.state import BattleSnakeState
