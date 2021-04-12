# Partially taken from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

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


class SearchNode:
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position: BoardCoord = None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


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
        self._add_body(board_json)

    def get_cell(self, x, y) -> BattleSnakeCell:
        return self.cells[self.height - y - 1][x]

    def get_cell_from_coord(self, coord: BoardCoord):
        return self.get_cell(coord.x, coord.y)

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

    def _add_body(self, board_json):
        for body_seg in board_json["you"]["body"]:
            self._set_cell(body_seg["x"], body_seg["y"], BattleSnakeCellType.BODY)

    def _is_valid(self, pos: BoardCoord):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

    def _is_empty(self, pos: BoardCoord):
        return self.get_cell_from_coord(pos).type == BattleSnakeCellType.EMPTY

    def get_empty_neighbours(self, pos: BoardCoord):
        neighbour_offsets = [BoardCoord(-1, 0), BoardCoord(1, 0), BoardCoord(0, -1), BoardCoord(0, 1)]
        neighbours = []
        for offset in neighbour_offsets:  # Adjacent squares
            # Get position
            neighbour_pos = pos + offset

            # Make sure within range and empty
            if not self._is_valid(neighbour_pos) and self._is_empty(neighbour_pos):
                continue

            neighbours.append(neighbour_pos)

        return neighbours

    @staticmethod
    def get_path(self, a: BoardCoord, b: BoardCoord):

        neighbour_offsets = [BoardCoord(-1, 0), BoardCoord(1, 0), BoardCoord(0, -1), BoardCoord(0, 1)]

        def astar(start, end):
            """Returns a list of tuples as a path from the given start to the given end in the given maze"""

            # Create start and end node
            start_node = SearchNode(None, start)
            start_node.g = start_node.h = start_node.f = 0
            end_node = SearchNode(None, end)
            end_node.g = end_node.h = end_node.f = 0

            # Initialize both open and closed list
            open_list = []
            closed_list = []

            # Add the start node
            open_list.append(start_node)

            # Loop until you find the end
            while len(open_list) > 0:

                # Get the current node
                current_node = open_list[0]
                current_index = 0
                for index, item in enumerate(open_list):
                    if item.f < current_node.f:
                        current_node = item
                        current_index = index

                # Pop current off open list, add to closed list
                open_list.pop(current_index)
                closed_list.append(current_node)

                # Found the goal
                if current_node == end_node:
                    path = []
                    current = current_node
                    while current is not None:
                        path.append(current.position)
                        current = current.parent
                    return path[::-1]  # Return reversed path

                # Generate children
                children = []
                for offset in neighbour_offsets:  # Adjacent squares

                    # Get node position
                    node_position = current_node.position + offset

                    # Make sure within range
                    if not self.is_valid(offset):
                        continue

                    # Make sure walkable terrain
                    if self.get_cell(node_position).type == BattleSnakeCellType.DANGER:
                        continue

                    # Create new node
                    new_node = SearchNode(current_node, node_position)

                    # Append
                    children.append(new_node)

                # Loop through children
                for child in children:

                    # Child is on the closed list
                    for closed_child in closed_list:
                        if child == closed_child:
                            continue

                    # Create the f, g, and h values
                    child.g = current_node.g + 1
                    child.g = self.dist(child.position, end_node.position)
                    child.f = child.g + child.h

                    # Child is already in the open list
                    for open_node in open_list:
                        if child == open_node and child.g > open_node.g:
                            continue

                    # Add the child to the open list
                    open_list.append(child)

        return astar(a, b)

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
