from collections import namedtuple

from agent.actions.action import BattleSnakeAction
from agent.environment.cell import BattleSnakeCellType, BattleSnakeCell, cell_symbols

BoardCoord = namedtuple("BoardPoint", "x y")



class BattleSnakeBoard:
    def __init__(self, board_json: dict):
        self.width = board_json["board"]["width"]
        self.height = board_json["board"]["height"]
        self.cells = \
            [
                [BattleSnakeCell(x, y, BattleSnakeCellType.EMPTY) for x in range(self.width)]
                for y in range(self.height)
            ]

        self.food = []

        self._add_food(board_json)
        self._add_danger(board_json)

    def get_cell(self, x, y) -> BattleSnakeCell:
        return self.cells[self.height - y - 1][x]

    def _set_cell(self, x, y, t: BattleSnakeCellType):
        self.cells[self.height - y - 1][x] = BattleSnakeCell(x, y, t)

    def _add_food(self, board_json):
        for food in board_json["board"]["food"]:
            current_food = BoardCoord(food["x"], food["y"])
            self._set_cell(current_food.x, current_food.y, BattleSnakeCellType.FOOD)
            self.food.append(current_food)

    def _add_danger(self, board_json):
        for snake in board_json["board"]["snakes"]:
            for body_seg in snake["body"]:
                self._set_cell(body_seg["x"], body_seg["y"], BattleSnakeCellType.DANGER)

    # BFS Pathfinding on grid from a to b
    @staticmethod
    def next_direction_to(a: BoardCoord, b: BoardCoord):

        heuristic = BattleSnakeBoard.dist

        return BattleSnakeAction.DOWN


    # Manhattan distance because we're locked to a grid
    @staticmethod
    def dist(a: BoardCoord, b: BoardCoord):
        return abs(a.x - b.x) + abs(a.y - b.y)

    def print_board(self):
        print("BOARD: ")
        out_str = ""
        for row in self.cells:
            for cell in row:
                out_str += cell_symbols[cell.type] + " "
            out_str += "\n"
        print(out_str)
