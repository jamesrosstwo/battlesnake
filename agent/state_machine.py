from agent.agent import BattleSnakeAgent
from agent.states.state import BattleSnakeState


class BattleSnakeStateMachine:
    def __init__(self, owner: BattleSnakeAgent):
        self.owner = owner
        self.current_state: BattleSnakeState = BattleSnakeFoodState.Instance
        self.previous_state: BattleSnakeState = None

    def change_state(self, new_state: BattleSnakeState):
        self.previous_state = self.current_state
        if self.current_state:
            self.current_state.exit(self.owner)
        self.current_state = new_state
        if self.current_state:
            self.current_state.enter(self.owner)

    def update(self):
        self.current_state.execute()

    def revert_to_last_state(self):
        if self.previous_state:
            self.change_state(self.previous_state)
