#!/usr/bin/python

from agent import Agent
from agent_penalized import AgentPenalized
from agent_state import AgentState
from environment import Environment
from pprint import pprint
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description='Mundo de la aspiradora.')
    parser.add_help()
    parser.add_argument('FILE', type=str, help='archivo con el layout del mundo en formato JSON')
    parser.add_argument('-x', type=int, help='posición en x de la aspiradora', default=0)
    parser.add_argument('-y', type=int, help='posición en y de la aspiradora', default=0)
    parser.add_argument('--agent', type=str, help='tipo de agente; valores aceptados simple (default), state y penalized', default='simple')
    args = parser.parse_args()
    show(args)

def show(args: argparse.Namespace) -> None:
    env = Environment.load_layout(args.FILE)
    if args.agent == 'simple':
        agent = Agent(env, args.x, args.y)
    elif args.agent == 'state':
        agent = AgentState(env, args.x, args.y)
    elif args.agent == 'penalized':
        agent = AgentPenalized(env, args.x, args.y)
    agent.clean_room()
    pprint(agent.log, sort_dicts=False)

if __name__ == '__main__':
    main()
    
