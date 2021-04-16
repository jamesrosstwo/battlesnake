from agent.actions.action import get_action_to
from agent.environment.board import BattleSnakeBoard
from agent.environment.coord import BoardCoord
from agent.singleton import Singleton
from agent.states.state import BattleSnakeState
from agent.states.state_avoid import BattleSnakeAvoidState


def try_safe_food_paths(board, entity, food_by_dist):
    path = None
    for food in food_by_dist:
        try:
            try_path = board.get_safe_path(entity.pos, food)
            path = try_path
            print("found safe path")
            break
        except KeyError:
            continue  # No path

    return path


def try_food_paths(board, entity, food_by_dist):
    path = None
    for food in food_by_dist:
        try:
            try_path = board.get_path(entity.pos, food)
            path = try_path
            break
        except KeyError:
            continue  # No path

    return path


@Singleton
class BattleSnakeFoodState(BattleSnakeState):
    def enter(self, entity):
        pass

    def execute(self, entity):
        board = entity.board
        food_by_dist = sorted(board.food, key=lambda x: BattleSnakeBoard.dist(entity.pos, x))

        path = try_safe_food_paths(board, entity, food_by_dist)
        if path is None:
            path = try_food_paths(board, entity, food_by_dist)

        if path is None:
            entity.state_machine.change_state(BattleSnakeAvoidState.instance())
        next_node = BoardCoord(*path[0])
        d = next_node - entity.pos
        return get_action_to(d)

    def exit(self, entity):
        pass
