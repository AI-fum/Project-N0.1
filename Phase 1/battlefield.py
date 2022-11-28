#map.py
class Battlefield:
    #map_array
    matrix: list[list[str]]
    points: list[tuple[int, int]]
    def __init__(self, height: int, width: int, matrix=[]):
        self.map = matrix
        self.width = width
        self.height = height
        self.points = []

    def check_out_of_bounds(self, y: int, x: int) -> bool:
        return x >= self.width or x < 0 or y >= self.height or y < 0

    def is_block(self, y: int, x: int):
        return self.battlefield.[y][x].lower() == 'x'

    def set_points(self, points):
        self.points = points

    def get_item(self, y, x) -> str:
        return self.battlefield.[y][x]

    def append_row(self, row: list[str]) -> None:
        if len(row) != self.width:
            raise ValueError('Invalid size of columns in this row:\n', str(row))
        self.battlefield.append(row)
