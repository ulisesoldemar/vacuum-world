from agent import Agent
from environment import Environment
from actions import *


class AgentPenalized(Agent):
    def __init__(self,
                 env: Environment,
                 x_pos: int = 0, y_pos: int = 0) -> None:
        super().__init__(env, x_pos, y_pos)
        self.energy = 2000

    def action(self, action: str) -> None:
        if action == SUCK:
            self.env.layout[self.x][self.y] -= 1
            self.env.total_dirt -= 1
            self.score += 5
            self.energy -= 3
        else:
            if action == UP:
                self.x -= 1
            elif action == DOWN:
                self.x += 1
            elif action == LEFT:
                self.y -= 1
            elif action == RIGHT:
                self.y += 1
            self.energy -= 1
        self.moves += 1

    def clean_room(self) -> None:
        super().clean_room()
        self.log['Energy left'] = self.energy
