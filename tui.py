from agent import Agent
from environtment import Environment
from evaluator import Evaluator
from random import randint

import curses
from curses import wrapper

from time import sleep

def matrix_string(m: list) -> str:
    x = ''
    for row in m:
        x += ' '.join(str(item) for item in row)
        x += "\n"
    return x

def main(stdscr) -> None:
    rows = randint(0, 5)
    cols = randint(0, 5)
    x = randint(0, 5) 
    y = randint(0, 5)
    env = Environment(rows, cols, x, y)
    agent = Agent()
    evaluator = Evaluator()
    while env.total_dirt:
        stdscr.clear()
        matrix = env.layout
        stdscr.addstr(0, 0, matrix_string(matrix))
        agent.perceive(env)
        action = agent.think()
        env.accept_action(action)
        evaluator.eval(action, env)
        stdscr.refresh()
        sleep(0.5)
    
    curses.endwin()
    quit()
    
if __name__ == '__main__':
    wrapper(main)

