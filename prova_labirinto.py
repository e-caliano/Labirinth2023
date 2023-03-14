import json
from PIL import Image

class Maze:
    def __init__(self, maze_input):
        if isinstance(maze_input, str):
            self.load_from_file(maze_input)
        elif isinstance(maze_input, Image.Image):
            self.load_from_image(maze_input)
        else:
            raise ValueError("Invalid maze input type")

    def load_from_file(self, file_path):
        with open(file_path, 'r') as f:
            maze_data = json.load(f)

        self.width = maze_data['larghezza']
        self.height = maze_data['altezza']
        self.starts = maze_data['iniziali']
        self.end = maze_data['finale']
        self.costs = {(x, y): 0 for x in range(self.width) for y in range(self.height)}

        for cost in maze_data['costi']:
            self.costs[(cost[0][0], cost[0][1])] = cost[1]

        walls = []

        for wall in maze_data['pareti']:
            x, y = wall['posizione']
            length = wall['lunghezza']

            if wall['orientamento'] == 'H':
                walls.extend([(x+i, y) for i in range(length)])
            else:
                walls.extend([(x, y+i) for i in range(length)])

        self.walls = set(walls)

    def load_from_image(self, image):
        self.width, self.height = image.size
        self.starts = []
        self.costs = {}
        pixels = image.load()

        for x in range(self.width):
            for y in range(self.height):
                if pixels[x, y] == (255, 0, 0):
                    self.end = (x, y)
                elif pixels[x, y] == (0, 255, 0):
                    self.starts.append((x, y))
                elif pixels[x, y] != (0, 0, 0):
                    gray_value = pixels[x, y][0]
                    self.costs[(x, y)] = (gray_value // 16) + 1

        self.walls = set((x, y) for x in range(self.width) for y in range(self.height) if pixels[x, y] == (0, 0, 0))

    def find_path(self, start):
        queue = [(start, [], 0)]
        visited = set()

        while queue:
            pos, path, cost_so_far = queue.pop(0)

            if pos == self.end:
                return path, cost_so_far

            if pos in visited or pos in self.walls:
                continue

            visited.add(pos)

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = pos[0] + dx, pos[1] + dy
                new_cost = cost_so_far + self.costs[(x, y)]
                new_path = path + [(x, y)]

                queue.append(((x, y), new_path, new_cost))

        return None, None

    def find_all_paths(self):
        paths = {}

        for start in self.starts:
            path, cost = self.find_path(start)

            if path is None:
                paths[str(start)] = "No path found"
            else:
                paths[str(start)] = {"path": path, "cost": cost}

        return paths