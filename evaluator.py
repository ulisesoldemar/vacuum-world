from actions import *
import time

class Evaluator:
    def __init__(self) -> None:
        self.consumed_energy = 0
        self.start_time = 0
        self.stop_time = 0

    def eval(self, action: str) -> None:
        if action == SUCK:
            self.consumed_energy += 2
        elif action != IDLE:
            self.consumed_energy += 1
    
    def start(self) -> float:
        self.start_time = time.perf_counter()
        return self.start_time

    def stop(self) -> float:
        self.stop_time = time.perf_counter() - self.start_time
        return self.stop_time

