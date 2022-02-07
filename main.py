from agent import Agent
from agent_state import AgentState
from environment import Environment
from evaluator import Evaluator
from random import randint
from time import sleep
from os import system


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
        agent = AgentState()
        evl = Evaluator()
        while env.total_dirt:
            system('clear')
            env.show()
            print('Agent position: ', (agent.x, agent.y), end='\t| ')
            agent.perceive(env)
            agent.not_visited()
            action = agent.think()
            print('Action: ', action)
            agent.action(action, env)
            evl.eval(action, env)
            print('Consumed energy: ', evl.consumed_energy, end='\t| ')
            print('Dirty degree: ', evl.dirty_degree)
            sleep(0.5)


if __name__ == '__main__':
    main()
