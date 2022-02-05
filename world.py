from random import randint

# actions
CLEAN = 'clean'
UP    = 'up'
DOWN  = 'down'
LEFT  = 'left'
RIGHT = 'right'


class World:
    def __init__(self, rows: int, cols: int) -> None:
        self.layout = []
        self.rows = rows
        self.cols = cols
        self.dirty_rooms = 0
        for _ in range(rows):
            rooms = [randint(0, 1) for _ in range(cols)]
            self.layout.append(rooms)
            self.dirty_rooms += sum(rooms)

    def show(self):
        for i in range(self.rows):
            print(self.layout[i])