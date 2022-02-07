from environment import Environment
from actions import *


class Evaluator:
    def __init__(self) -> None:
        self.dirty_degree = 0
        self.consumed_energy = 0

    def eval(self, action: str, env: Environment) -> None:
        if action == SUCK:
            self.consumed_energy += 2
        elif action != IDLE:
            self.consumed_energy += 1

        for x in range(env.rows):
            for y in range(env.cols):
                da = env.dirt_amount(x, y)
                self.dirty_degree += da*da
