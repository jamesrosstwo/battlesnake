from abc import ABC, abstractmethod


class BattleSnakeState(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def enter(self, entity: "BattleSnakeAgent"):
        pass

    @abstractmethod
    def execute(self, entity: "BattleSnakeAgent"):
        pass

    @abstractmethod
    def exit(self, entity: "BattleSnakeAgent"):
        pass


from agent.agent import BattleSnakeAgent
