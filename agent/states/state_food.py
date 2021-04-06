from agent.actions.action import BattleSnakeAction
from agent.environment.board import BattleSnakeBoard
from agent.singleton import Singleton
from agent.states.state import BattleSnakeState


@Singleton
class BattleSnakeFoodState(BattleSnakeState):
    def enter(self, entity):
        pass

    def execute(self, entity):
        board = entity.board
        nearest_food = board.food[0]
        min_dist = BattleSnakeBoard.dist(entity.pos, nearest_food)
        for food in board.food[1:]:
            d = BattleSnakeBoard.dist(entity.pos, food) < min_dist
            if d < min_dist:
                min_dist = d
                nearest_food = food

        return BattleSnakeBoard.next_direction_to(entity.pos, nearest_food)

    def exit(self, entity):
        pass


