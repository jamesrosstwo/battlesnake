import random

from agent.actions.action import BattleSnakeAction
from agent.environment.board import BattleSnakeBoard
from agent.singleton import Singleton
from agent.states.state import BattleSnakeState


@Singleton
class BattleSnakeWanderState(BattleSnakeState):
    def enter(self, entity):
        pass

    def execute(self, entity):
        board = entity.board
        pos = entity.pos
        empty_neighbours = board.get_walkable_neighbours(pos)
        possible_moves = []

        for neighbour in empty_neighbours:
            d = neighbour - pos
            if d.x > 0:
                possible_moves.append(BattleSnakeAction.RIGHT)
            elif d.x < 0:
                possible_moves.append(BattleSnakeAction.LEFT)
            elif d.y > 0:
                possible_moves.append(BattleSnakeAction.UP)
            else:
                possible_moves.append(BattleSnakeAction.DOWN)

        return random.choice(possible_moves)

    def exit(self, entity):
        pass
