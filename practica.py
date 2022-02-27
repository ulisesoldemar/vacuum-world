from random import randint, choice
from time import sleep
import os
import json

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
SUCK = 'suck'
IDLE = 'idle'


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

    def clean(self, env: Environment) -> None:
        while env.total_dirt:
            self.do_step(env)


def main() -> None:
    try:
        filename = 'data.json'
        with open(filename, 'r') as file:
            env = Environment.from_json(file)
    except FileNotFoundError:
        print('No se encontró el archivo {}. Se generará un entorno aleatorio.'.format(
            filename))
        rows = randint(1, 5)
        cols = randint(1, 5)
        env = Environment(rows, cols)
    finally:
        agent = Agent()
        evl = Evaluator()
        while env.total_dirt:
            os.system('clear')
            env.show()
            print('Agent position: ', (agent.x, agent.y), end='\t| ')
            agent.perceive(env)
            action = agent.think()
            print('Action: ', action)
            agent.action(action, env)
            evl.eval(action, env)
            print('Consumed energy: ', evl.consumed_energy, end='\t| ')
            print('Dirty degree: ', evl.dirty_degree)
            sleep(0.5)


if __name__ == '__main__':
    main()
