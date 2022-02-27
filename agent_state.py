from re import S
from environment import Environment
from agent import Agent
from actions import *


class AgentState(Agent):
    def __init__(self,
                 env: Environment,
                 x_pos: int = 0, y_pos: int = 0) -> None:
        super().__init__(env, x_pos, y_pos)
        self.visited = set()
        self.dirty_rooms = set()

    def action(self, action: str) -> None:
        super().action(action)
        self.visited.add((self.x, self.y))

   # Sensor del ambiente
    def perceive(self) -> None:
        self.dirty = self.env.dirt_amount(self.x, self.y) > 0
        dirty_rooms = set()
        self.valid_moves.clear()
        if self.x-1 >= 0:
            self.valid_moves.add(UP)
            if self.env.dirt_amount(self.x-1, self.y) > 0:
                dirty_rooms.add(UP)
        if self.x+1 < self.env.rows:
            self.valid_moves.add(DOWN)
            if self.env.dirt_amount(self.x+1, self.y) > 0:
                dirty_rooms.add(DOWN)
        if self.y-1 >= 0:
            self.valid_moves.add(LEFT)
            if self.env.dirt_amount(self.x, self.y-1) > 0:
                dirty_rooms.add(LEFT)
        if self.y+1 < self.env.cols:
            self.valid_moves.add(RIGHT)
            if self.env.dirt_amount(self.x, self.y+1) > 0:
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
