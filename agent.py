from copy import deepcopy
from environment import Environment
from evaluator import Evaluator
from actions import *
from random import choice
from json import *


class Agent:
    def __init__(self,
                 env: Environment,
                 x_pos: int = 0, y_pos: int = 0) -> None:
        self.dirty = False  # Bandera de suciedad en cuarto
        self.x = x_pos
        self.y = y_pos
        self.env = env
        self.valid_moves = set()
        self.score = 0
        self.moves = 0

        self.log = dict()
        self.log['Init layout'] = deepcopy(env.layout)
        self.log['Init X'] = x_pos
        self.log['Init Y'] = y_pos

    # Sensor del ambiente
    def perceive(self) -> None:
        self.dirty = self.env.dirt_amount(self.x, self.y) > 0
        self.valid_moves.clear()
        if self.x-1 >= 0:
            self.valid_moves.add(UP)
        if self.x+1 < self.env.rows:
            self.valid_moves.add(DOWN)
        if self.y-1 >= 0:
            self.valid_moves.add(LEFT)
        if self.y+1 < self.env.cols:
            self.valid_moves.add(RIGHT)

    # Decide la siguiente acción
    def think(self) -> str:
        return SUCK if self.dirty else choice(list(self.valid_moves))

    # Realiza la acción en base a su información
    def action(self, action: str) -> None:
        if action == SUCK:
            self.env.layout[self.x][self.y] -= 1
            self.env.total_dirt -= 1
            self.score += 3
        elif action == UP:
            self.x -= 1
        elif action == DOWN:
            self.x += 1
        elif action == LEFT:
            self.y -= 1
        elif action == RIGHT:
            self.y += 1
        self.moves += 1

    def clean_room(self) -> None:
        evl = Evaluator()
        evl.start()
        while self.env.total_dirt:
            self.perceive()
            action = self.think()
            self.action(action)
            evl.eval(action)
        total_time = evl.stop()

        self.log['Final layout'] = self.env.layout
        self.log['Total moves'] = self.moves
        self.log['Agent score'] = self.score
        self.log['Total time'] = total_time
        self.log['Consumed energy'] = evl.consumed_energy
        self.log['Performance'] = self.score / evl.consumed_energy