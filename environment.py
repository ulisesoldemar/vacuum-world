from random import randint
from actions import *
import json


class Environment:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

    @classmethod
    def load_layout(cls, filename: str):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                cls.layout = data['layout']
        except FileNotFoundError:
            print('No se encontró el archivo {}.'.format(filename))
        except KeyError:
            print('No se encontró el layout en el archivo.')
        
        rows = len(cls.layout)
        cols = len(cls.layout[0])
        cls.total_dirt = sum([sum(row) for row in cls.layout])
        return cls(rows, cols)

    def show(self) -> None:
        for i in range(self.rows):
            print(self.layout[i])

    def random_layout(self, max_dirt = 1) -> None:
        self.layout = []
        self.rows = randint(1, 5)
        self.cols = randint(1, 5)
        for _ in range(self.rows):
            rooms = [randint(0, max_dirt) for _ in range(self.cols)]
            self.layout.append(rooms)
            self.total_dirt += sum(rooms)

    def dirt_amount(self, x, y) -> int:
        return self.layout[x][y]
