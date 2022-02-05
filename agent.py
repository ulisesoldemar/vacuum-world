from world import *


class Agent:
    def __init__(self, x_pos: int, y_pos: int, world: World) -> None:
        # attributes
        self.x = x_pos
        self.y = y_pos
        self.world = world
        self.visited = set()
        # counters
        self.score = 0
        self.rooms_left = world.dirty_rooms
        self.rooms_cleaned = 0
        # initial room
        self.visited.add((self.x, self.y))

    def possible_steps(self) -> list:
        # potential movements
        allowed = []
        # verification
        if self.world.layout[self.y][self.x]:
            allowed.append(CLEAN)
        if self.y-1 >= 0:
            allowed.append(UP)
        if self.y+1 < self.world.rows:
            allowed.append(DOWN)
        if self.x-1 >= 0:
            allowed.append(LEFT)
        if self.x+1 < self.world.cols:
            allowed.append(RIGHT)
        # return potential movements
        return allowed

    def perform_action(self, action: str) -> None:
        print((self.x, self.y), action)
        if action == CLEAN:
            self.world.layout[self.y][self.x] = 0
            self.score += 10
            self.rooms_left -= 1
        elif action == UP:
            self.y -= 1
            self.score -= 1
        elif action == DOWN:
            self.y += 1
            self.score -= 1
        elif action == LEFT:
            self.x -= 1
            self.score -= 1
        elif action == RIGHT:
            self.x += 1
            self.score -= 1
        # save room
        self.visited.add((self.x, self.y))
