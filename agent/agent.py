from agent.state_machine import BattleSnakeStateMachine
from agent.actions.action import BattleSnakeAction



class BattleSnakeAgent:
    def __init__(self):
        self.state_machine = BattleSnakeStateMachine(self)

    def select_state(self, board) -> "BattleSnakeState":
        pass

    def parse_board(self, board):
        pass

    def act(self, board) -> "BattleSnakeAction":
        print(board)
        # parsed_board = self.parse_board(board)
        # self.state_machine.change_state(self.select_state(parsed_board))
        # return self.state_machine.calculate_action()
        return BattleSnakeAction.RIGHT


from agent.states.state import BattleSnakeState
