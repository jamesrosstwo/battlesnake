from agent.actions.action import BattleSnakeAction, get_dir_to
from agent.environment.board import BattleSnakeBoard, BoardCoord
from agent.singleton import Singleton
from agent.states.state import BattleSnakeState


@Singleton
class BattleSnakeFoodState(BattleSnakeState):
    def enter(self, entity):
        pass

    def execute(self, entity):
        board = entity.board
        food_by_dist = sorted(board.food, key=lambda x: BattleSnakeBoard.dist(entity.pos, x))

        path = None
        for food in food_by_dist:
            try:
                try_path = board.get_path(entity.pos, food)
            except KeyError:
                continue  # No path
            path = try_path

        next_node = BoardCoord(*path[0])
        d = next_node - entity.pos
        return get_dir_to(d)

    def exit(self, entity):
        pass
