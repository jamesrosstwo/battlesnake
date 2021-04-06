from collections import namedtuple

from agent.actions.action import BattleSnakeAction
from agent.environment.cell import BattleSnakeCellType, BattleSnakeCell, cell_symbols

class BoardCoord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return BoardCoord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return BoardCoord(self.x - other.x, self.y - other.y)


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

    def _is_valid(self, pos: BoardCoord):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    # BFS Pathfinding on grid from a to b
    # Template: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
    @staticmethod
    def next_direction_to(a: BoardCoord, b: BoardCoord):

        # neighbour_offsets = [BoardCoord(-1, 0), BoardCoord(1, 0), BoardCoord(0, -1), BoardCoord(0, 1)]
        #
        # # Function to print a BFS of graph
        # def bfs(self, s):
        #     # Create a queue for BFS
        #     queue = [s]
        #
        #     while queue:
        #
        #         # Dequeue a vertex from
        #         # queue and print it
        #         s = queue.pop(0)
        #         print(s, end=" ")
        #
        #         # Get all adjacent vertices of the
        #         # dequeued vertex s. If a adjacent
        #         # has not been visited, then mark it
        #         # visited and enqueue it
        #         for offset in neighbour_offsets:
        #             new_pos = s + offset
        #             new_cell = self.get_cell(new_pos)
        #             if not new_cell.seen:
        #                 queue.append(new_cell)
        #                 new_cell.seen = True
        #
        # heuristic = BattleSnakeBoard.dist

        d = b - a
        if d.x > 0:
            return BattleSnakeAction.RIGHT
        elif d.x < 0:
            return BattleSnakeAction.LEFT

        if d.y > 0:
            return BattleSnakeAction.UP
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
