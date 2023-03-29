import heapq
from typing import List, Tuple
from PIL import Image, ImageDraw
from labirinto import Labirinto


def find_paths(matrix: List[List[int]], start_points: List[Tuple[int, int]], end_point: Tuple[int, int]) -> Tuple[List[List[Tuple[int, int]]], List[float]]:
    """
    Trova tutti i percorsi dai punti di partenza al punto di arrivo con i relativi costi dei percorsi,
    dove la somma del costo del percorso deve essere data dalla somma dei costi delle caselle pesate più il percorso in pixel.

    :param matrix: una matrice bidimensionale che rappresenta il labirinto.
    :param start_points: una lista di tuple contenente i punti di partenza.
    :param end_point: una tupla contenente il punto di arrivo.
    :return: una tupla contenente una lista di tutti i percorsi trovati e una lista di tutti i relativi costi.
    """
    rows, cols = len(matrix), len(matrix[0])
    pq = [(0, start, []) for start in start_points]  # priority queue of (cost, current position, path)
    visited = set(start_points)
    paths = []
    costs = []

    while pq:
        cost, curr, path = heapq.heappop(pq)

        if curr == end_point:
            paths.append(path + [curr])
            costs.append(cost)
            continue

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = curr[0] + dr, curr[1] + dc

            if r < 0 or r >= rows or c < 0 or c >= cols:
                continue

            if matrix[r][c] == 0 or (r, c) in visited:
                continue

            new_cost = cost + matrix[r][c]
            new_path = path + [curr]

            heapq.heappush(pq, (new_cost, (r, c), new_path))
            visited.add((r, c))

    return paths, costs


def find_cheapest_path(matrix: List[List[int]], start_points: List[Tuple[int, int]], end_point: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Trova il percorso con il costo minore tra tutti quelli trovati dalla funzione find_paths().

    :param matrix: una matrice bidimensionale che rappresenta il labirinto.
    :param start_points: una lista di tuple contenente i punti di partenza.
    :param end_point: una tupla contenente il punto di arrivo.
    :return: una lista di tuple che rappresenta il percorso con il costo minore.
    """
    paths, costs = find_paths(matrix, start_points, end_point)

    if not paths:
        return []

    cheapest_path_index = costs.index(min(costs))
    return paths[cheapest_path_index]


from PIL import Image, ImageDraw


def draw_paths_on_image(image_path, paths):
    """
    Disegna i percorsi trovati sull'immagine del labirinto.

    :param image_path: il percorso del file immagine del labirinto
    :param paths: una lista di percorsi da disegnare sull'immagine
    """
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']

    for i, path in enumerate(paths):
        color = colors[i % len(colors)]
        for j in range(len(path) - 1):
            x1, y1 = path[j]
            x2, y2 = path[j + 1]
            draw.line((y1, x1, y2, x2), fill=color, width=1)

    img.show()


labirinto = Labirinto("30-20_marked.tiff")
labirinto.gestisci_input()

a, b = find_paths(labirinto.maze, labirinto.start, labirinto.end)
print(a)
print(b)

c = find_cheapest_path(labirinto.maze, labirinto.start, labirinto.end)
print(c)

draw_paths_on_image("/Users/edoardocaliano/Desktop/Labyrinth/indata/30-20_marked.tiff", a)