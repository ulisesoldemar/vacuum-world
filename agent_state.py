from re import S
from environment import Environment
from agent import Agent
from actions import *


class AgentState(Agent):
    def __init__(self) -> None:
        super().__init__()
        self.visited = set()
        self.dirty_rooms = set()

    def action(self, action: str, env: Environment) -> None:
        super().action(action, env)
        self.visited.add((self.x, self.y))

   # Sensor del ambiente
    def perceive(self, env: Environment) -> None:
        self.dirty = env.dirt_amount(self.x, self.y) > 0
        dirty_rooms = set()
        self.valid_moves.clear()
        if self.x-1 >= 0:
            self.valid_moves.add(UP)
            if env.dirt_amount(self.x-1, self.y) > 0:
                dirty_rooms.add(UP)
        if self.x+1 < env.rows:
            self.valid_moves.add(DOWN)
            if env.dirt_amount(self.x+1, self.y) > 0:
                dirty_rooms.add(DOWN)
        if self.y-1 >= 0:
            self.valid_moves.add(LEFT)
            if env.dirt_amount(self.x, self.y-1) > 0:
                dirty_rooms.add(LEFT)
        if self.y+1 < env.cols:
            self.valid_moves.add(RIGHT)
            if env.dirt_amount(self.x, self.y+1) > 0:
                dirty_rooms.add(RIGHT)
        dirty_rooms.intersection_update(self.not_visited())
        if len(dirty_rooms) > 0:
            self.valid_moves = dirty_rooms

    def not_visited(self) -> set:
        not_visited = set()
        if (self.x-1, self.y) not in self.visited:
            not_visited.add(UP)
        if (self.x+1, self.y) not in self.visited:
            not_visited.add(DOWN)
        if (self.x, self.y-1) not in self.visited:
            not_visited.add(LEFT)
        if (self.x, self.y+1) not in self.visited:
            not_visited.add(RIGHT)

        return not_visited
