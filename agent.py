from environment import Environment
from actions import *
from random import choice


class Agent:
    def __init__(self,
                 x_pos: int = 0, y_pos: int = 0,) -> None:
        self.dirty = False  # Bandera de suciedad en cuarto
        self.x = x_pos
        self.y = y_pos
        self.valid_moves = set()

    # Sensor del ambiente
    def perceive(self, env: Environment) -> None:
        self.dirty = env.dirt_amount(self.x, self.y) > 0
        self.valid_moves.clear()
        if self.x-1 >= 0:
            self.valid_moves.add(UP)
        if self.x+1 < env.rows:
            self.valid_moves.add(DOWN)
        if self.y-1 >= 0:
            self.valid_moves.add(LEFT)
        if self.y+1 < env.cols:
            self.valid_moves.add(RIGHT)
    
    # Decide la siguiente acción
    def think(self) -> str:
        return SUCK if self.dirty else choice(list(self.valid_moves))

    # Realiza la acción en base a su información
    def action(self, action: str, env: Environment) -> None:
        if action == SUCK:
            env.layout[self.x][self.y] -= 1
            env.total_dirt -= 1
        elif action == UP:
            self.x -= 1
        elif action == DOWN:
            self.x += 1
        elif action == LEFT:
            self.y -= 1
        elif action == RIGHT:
            self.y += 1
    
    def do_step(self, env: Environment) -> None:
        self.perceive(env)
        action = self.think()
        self.action(action)
    
    def clean(self, env: Environment):
        while env.total_dirt:
            self.do_step(env)



