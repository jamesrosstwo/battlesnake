from agent.environment.cell import BattleSnakeCellType, BattleSnakeCell, cell_symbols


class BattleSnakeBoard:
    def __init__(self, board_json: dict):
        self.width = board_json["board"]["width"]
        self.height = board_json["board"]["height"]
        self.cells = \
            [
                [BattleSnakeCell(x, y, BattleSnakeCellType.EMPTY) for x in range(self.width)]
                for y in range(self.height)
            ]

        self._add_food(board_json)
        self._add_danger(board_json)

    def get_cell(self, x, y):
        return self.cells[self.height - y - 1][x]

    def _set_cell(self, x, y, type):
        self.cells[self.height - y - 1][x] = BattleSnakeCell(x, y, type)

    def _add_food(self, board_json):
        for food in board_json["board"]["food"]:
            self._set_cell(food["x"], food["y"], BattleSnakeCellType.FOOD)

    def _add_danger(self, board_json):
        for snake in board_json["board"]["snakes"]:
            for body_seg in snake["body"]:
                self._set_cell(body_seg["x"], body_seg["y"], BattleSnakeCellType.DANGER)

    def print_board(self):
        print("BOARD: ")
        out_str = ""
        for row in self.cells:
            for cell in row:
                out_str += cell_symbols[cell.type] + " "
            out_str += "\n"
        print(out_str)
