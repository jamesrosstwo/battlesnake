from agent.singleton import Singleton
from agent.states.state import BattleSnakeState


@Singleton
class BattleSnakeFoodState(BattleSnakeState):
    def enter(self, entity):
        pass

    def execute(self, entity):
        pass

    def exit(self, entity):
        pass


