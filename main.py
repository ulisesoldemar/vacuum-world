from simple_agent import SimpleAgent
from world import World

# main
def main() -> None:
    # create environment
    world = World(2, 2)
    world.show()
    vacuum = SimpleAgent(1, 1, world)
    vacuum.clean_world()
    world.show()


# run main
if __name__ == '__main__':
    main()
