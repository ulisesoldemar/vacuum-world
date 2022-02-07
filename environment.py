from distutils.command.build import build
from random import randint
from actions import *
import json


class Environment:
    def __init__(self, rows: int, cols: int, max_dirt: int = 5) -> None:
        self.rows = rows
        self.cols = cols
        self.max_dirt = max_dirt
        self.layout = []
        self.total_dirt = 0
        self.change()

    @classmethod
    def from_json(cls, json_file):
        data = json.load(json_file)
        return cls(
            rows=data['rows'],
            cols=data['cols']
        )
    
    def load_layout(self, json_file):
        data = json.load(json_file)
        self.layout = data['layout']

    def show(self) -> None:
        for i in range(self.rows):
            print(self.layout[i])

    def change(self) -> None:
        self.layout.clear()
        for _ in range(self.rows):
            rooms = [randint(0, self.max_dirt) for _ in range(self.cols)]
            self.layout.append(rooms)
            self.total_dirt += sum(rooms)

    def dirt_amount(self, x, y) -> int:
        return self.layout[x][y]
