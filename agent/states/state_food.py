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
            d = BattleSnakeBoard.dist(entity.pos, food)
            if d < min_dist:
                min_dist = d
                nearest_food = food

        path = BattleSnakeBoard.get_path(entity.pos, nearest_food)
        next_node = path[1].position
        d = next_node - entity.pos
        if d.x > 0:
            return BattleSnakeAction.RIGHT
        elif d.x < 0:
            return BattleSnakeAction.LEFT

        if d.y > 0:
            return BattleSnakeAction.UP
        return BattleSnakeAction.DOWN

    def exit(self, entity):
        pass
