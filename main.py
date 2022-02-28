#!/usr/bin/python

from agent import Agent
from agent_penalized import AgentPenalized
from agent_state import AgentState
from environment import Environment
from pprint import pprint
import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser(description='Mundo de la aspiradora.')
    parser.add_argument(
        'FILE', type=str, help='archivo con el layout del mundo en formato JSON')
    parser.add_argument(
        '-x', type=int, help='posición en x de la aspiradora', default=0)
    parser.add_argument(
        '-y', type=int, help='posición en y de la aspiradora', default=0)
    parser.add_argument(
        '--agent', type=str, help='tipo de agente; valores aceptados simple (default), state y penalized', default='simple')
    parser.add_argument('--save', type=str,
                        help='archivo JSON donde se guardará la salida')
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
    else:
        print('no se reconce el tipo de agente. valores aceptados simple (default), state y penalized')
        return

    try:
        agent.clean_room()
        pprint(agent.log, sort_dicts=False)
    except IndexError:
        print('los valores de x y y deben estar en los límites del layout del archivo:')
        pprint(env.layout)

    if args.save:
        dump(args.save, args, agent.log)


def dump(filename: str, args: argparse.Namespace, log: dict) -> None:
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)

        data[args.FILE]['Agent type'] = args.agent
        data[args.FILE]['Run count'] += 1
        data[args.FILE]['Total performance'] += log['Performance']
        data[args.FILE]['Average performance'] = data[args.FILE]['Total performance'] / \
            data[args.FILE]['Run count']

        with open(filename, 'w') as json_file:
            json.dump(data, json_file)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = dict()
        log['Agent type'] = args.agent
        log['Run count'] = 1
        log['Total performance'] = log['Performance']
        log['Average performance'] = log['Performance']
        data[args.FILE] = log
        with open(filename, 'w') as json_file:
            json.dump(data, json_file)


if __name__ == '__main__':
    main()
