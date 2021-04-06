from agent.singleton import Singleton
from agent.states.state import BattleSnakeState


@Singleton
class BattleSnakeFoodState(BattleSnakeState):
    def enter(self, entity: "BattleSnakeAgent"):
        pass

    def execute(self, entity: "BattleSnakeAgent"):
        pass

    def exit(self, entity: "BattleSnakeAgent"):
        pass


from agent.agent import BattleSnakeAgent
