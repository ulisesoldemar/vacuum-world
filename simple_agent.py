from world import CLEAN
from agent import Agent
from random import choice

class SimpleAgent(Agent):

    def clean_world(self) -> None:
        # clean environment
        while self.rooms_left:
            # action
            allowed_steps = self.possible_steps()
            next_step = CLEAN if CLEAN in allowed_steps else choice(allowed_steps)
            self.perform_action(next_step)