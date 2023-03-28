import os
import json
from PIL import Image, ImageDraw
import networkx as nx
from typing import List, Tuple

class Labirinto:
    def __init__(self):
        self.maze = []
        self.start = []
        self.end = ()
        self.image = None


    def gestisci_input(self, percorso_file):
        # estrae il nome del file e l'estensione
        nome_file, estensione = os.path.splitext(percorso_file)

        # controllo l'estensione ed eseguo l'azione appropriata
        if estensione == '.json':
            # carico il labirinto dal file JSON
            with open(percorso_file) as json_file:
                data = json.load(json_file)
            self.json_to_maze(data)
        # controllo che l'estensione sia di tipo TIFF, JPEG O PNG
        elif estensione in ['.tiff', '.jpeg', '.png']:
            # carico il labirinto dall'immagine
            self.image = Image.open(percorso_file)
            self.image_to_maze()
        # in tutti gli altri casi non devo supportare l'estensione
        else:
            # gestione dell'errore se l'estensione non è supportata
            print("Estensione del file non supportata")


    def json_to_maze(self, data):

        if set(list(data.keys())) != {"larghezza", "altezza", "pareti", "iniziali", "finale", "costi"}:
            raise ValueError("Struttura file JSON non supportata")

        for i in range(data["altezza"]):
            maze_row = []
            for j in range(data["larghezza"]):
                maze_row.append(1)
            self.maze.append(maze_row)

        # Popola la matrice con le pareti
        for wall in data["pareti"]:
            if wall["orientamento"] == "H":
                for i in range(wall["lunghezza"]):
                    self.maze[wall["posizione"][0]][wall["posizione"][1] + i] = 0
            elif wall["orientamento"] == "V":
                for i in range(wall["lunghezza"]):
                    self.maze[wall["posizione"][0] + i][wall["posizione"][1]] = 0

        # Popola con le posizioni iniziali
        for iniziale in data["iniziali"]:
            i = iniziale[0]
            j = iniziale[1]
            self.start.append((i, j))


        # Popola con la posizione di arrivo
        i = data["finale"][0][0]
        j = data["finale"][0][1]
        self.end = (i, j)


        # Popolo con le caselle in scala di grigi
        for costo in data["costi"]:
            i = costo[0]
            j = costo[1]
            peso = costo[2] + 1
            self.maze[i][j] = peso

        self.maze_to_image()
        print(self.maze)



    def maze_to_image(self):
        # creazione di un'immagine vuota tramite Image, che abbia dimensione pari alla matrice che contiene il labirinto
        self.image = Image.new("RGB", (len(self.maze[0]), len(self.maze)))
        pixels = self.image.load()
        # Impostazione dei pixel dell'immagine in base alla matrice del labirinto
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 0:
                    # imposto il muro
                    pixels[j, i] = (0, 0, 0)  # muro = nero
                    # imposto il cammino
                elif self.maze[i][j] == 1:
                    pixels[j, i] = (255, 255, 255)  # cammino = bianco
                else:
                    # imposto il cammino pesato
                    pixels[j, i] = ((self.maze[i][j] - 1) * 16, (self.maze[i][j] - 1) * 16,
                                    (self.maze[i][j] - 1) * 16)  # cammino pesato = grigio scuro
        # imposto l'inizio e la fine del labirinto
        i = self.end[0]
        j = self.end[1]
        pixels[j, i] = (255, 0, 0)  # arrivo = rosso
        for st in self.start:
            i = st[0]
            j = st[1]
            pixels[j, i] = (0, 255, 0)  # partenza = verde
        self.image.show()

    # def image_to_maze(self):
    #     # Carica il file immagine
    #     # img = Image.open(image_file)
    #
    #     # Ottieni le dimensioni dell'immagine
    #     width, height = self.image.size
    #
    #     # Scansiona l'immagine pixel per pixel
    #     for y in range(height):
    #         row = []
    #         for x in range(width):
    #             pixel = self.image.getpixel((x, y))
    #
    #             # Verifica se il pixel è nero o bianco
    #             if pixel == (0, 0, 0):
    #                 row.append(0)  # Aggiungi un muro
    #             elif pixel == (255, 255, 255):
    #                 row.append(1)  # Aggiungi un corridoio
    #             else:
    #                 # Determina il costo associato al valore di grigio
    #                 gray_value = sum(pixel) // 3
    #                 if gray_value == 16:
    #                     cost = 2
    #                 elif gray_value == 32:
    #                     cost = 4
    #                 elif gray_value == 48:
    #                     cost = 6
    #                 elif gray_value == 64:
    #                     cost = 8
    #                 elif gray_value == 80:
    #                     cost = 10
    #                 elif gray_value == 96:
    #                     cost = 12
    #                 elif gray_value == 112:
    #                     cost = 14
    #                 elif gray_value == 128:
    #                     cost = 16
    #                 elif gray_value == 144:
    #                     cost = 18
    #                 elif gray_value == 160:
    #                     cost = 20
    #                 elif gray_value == 176:
    #                     cost = 22
    #                 elif gray_value == 192:
    #                     cost = 24
    #                 elif gray_value == 208:
    #                     cost = 26
    #                 elif gray_value == 224:
    #                     cost = 28
    #                 elif gray_value == 240:
    #                     cost = 30
    #                 else:
    #                     raise ValueError("Valore di grigio non valido: " + str(gray_value))
    #
    #                 row.append(cost)
    #
    #             # Verifica se il pixel è rosso o verde
    #             if pixel == (255, 0, 0):
    #                 self.start = [x, y]  # Salva il punto di inizio
    #             elif pixel == (0, 255, 0):
    #                 self.end = (x, y)  # Salva il punto di arrivo
    #
    #         self.maze.append(row)
    #
    #     # Salva l'immagine
    #     self.image = self.image.copy()
    #     print(self.start)
    #     print(self.end)


    def image_to_maze(self):
        # apre l'immagine e ottiene i dati dei pixel
        pixel = self.image.load()
        larghezza, altezza = self.image.size

        # inizializza la matrice del labirinto
        labirinto = []
        for i in range(altezza):
            labirinto.append([0] * larghezza)

        # analizza i pixel dell'immagine e costruisce la matrice del labirinto
        for y in range(altezza):
            for x in range(larghezza):
                r, g, b = pixel[x, y]
                # pixel nero = muro
                if r == 0 and g == 0 and b == 0:
                    labirinto[y][x] = 0
                # pixel bianco, verde o rosso = posizione attraversabile
                elif r == 255 and g == 255 and b == 255 or r == 0 and g == 255 and b == 0 or r == 255 and g == 0 and b == 0:
                    labirinto[y][x] = 1
                # pixel grigio = casella con costo
                else:
                    # determina il valore del pixel in scala di grigi
                    valore_grigio = int(round(0.2989 * r + 0.5870 * g + 0.1140 * b))
                    # determina il costo associato al valore del pixel
                    if valore_grigio == 16:
                        costo = 1
                    elif valore_grigio == 32:
                        costo = 2
                    elif valore_grigio == 48:
                        costo = 3
                    elif valore_grigio == 64:
                        costo = 4
                    elif valore_grigio == 80:
                        costo = 5
                    elif valore_grigio == 96:
                        costo = 6
                    elif valore_grigio == 112:
                        costo = 7
                    elif valore_grigio == 128:
                        costo = 8
                    elif valore_grigio == 144:
                        costo = 9
                    elif valore_grigio == 160:
                        costo = 10
                    elif valore_grigio == 176:
                        costo = 11
                    elif valore_grigio == 192:
                        costo = 12
                    elif valore_grigio == 208:
                        costo = 13
                    elif valore_grigio == 224:
                        costo = 14
                    elif valore_grigio == 240:
                        costo = 15
                    else:
                        raise ValueError("Valore di grigio non valido")
                    labirinto[y][x] = costo + 1  # associazione del costo in base al grigio, andando a sommare 1 poichè il grigio è anche un corridoio
        self.maze = labirinto
        print(self.maze)

    # def image_to_maze(self):
    #     """
    #     Questa funzione trasforma l'immagine in ingresso in una matrice
    #     costituita da:
    #         - 0 se il colore RGB dei pixel è nero, quindi rappresenta il muro del
    #           labirinto
    #         - 1 se il colore RGB dei pixel è bianco, verde o rosso.
    #         - un numero da 2 a 16 se il colore RGB è una tonalità di grigio, rappresentando in questo
    #           modo il peso di una casella
    #     """
    #
    #     # Converte l'immagine in una matrice di pixel
    #     pixel_matrice = self.image.load()
    #     # Inizializzo il numero di caselle rosse trovate nel labirinto
    #     num_caselle_rosse = 0
    #     # Scansiona i pixel dell'immagine per creare la matrice del labirinto
    #     for i in range(self.image.height):
    #         riga_labirinto = []
    #         for j in range(self.image.width):
    #             pixel = pixel_matrice[j, i]
    #             # Si converte il pixel in un numero, 0 se è un muro, 1 altrimenti
    #             if pixel == (255, 255, 255):
    #                 riga_labirinto.append(1)
    #             elif pixel == (0, 0, 0):  # Pixel nero
    #                 riga_labirinto.append(0)
    #             elif pixel == (0, 255, 0):  # Pixel verde
    #                 riga_labirinto.append(1)
    #                 self.start.append((i, j))
    #             elif pixel == (255, 0, 0):  # Pixel rosso
    #                 num_caselle_rosse += 1
    #                 riga_labirinto.append(1)
    #                 self.end = (i, j)
    #             elif pixel[0] == pixel[1] == pixel[2]:
    #                 # in tal caso utilizziamo il valore del pixel come peso
    #                 # infatti i pixel grigi sono sempre nella forma (x,x,x)
    #                 # si somma 1 così nel caso del pixel (16,16,16) si ottiene un peso pari a 2
    #                 # poiché il peso 1 è attribuito alle caselle bianche
    #                 riga_labirinto.append((pixel[0] // 16) + 1)
    #             # Se vi è un pixel diverso da tutti i casi precedenti allora si produce un errore,
    #             # poiché il labirinto non è rappresentato correttamente.
    #             else:
    #                 raise ValueError("L'immagine fornita non rappresenta correttamente il labirinto.")
    #         self.maze.append(riga_labirinto)

        # # Verifica della presenza di almeno un punto di partenza
        # if len(self.start) < 1:
        #     raise ValueError("L'immagine fornita non presenta alcun punto di partenza.")
        #
        # # Verifica della presenza di un unico punto di arrivo
        # if num_caselle_rosse == 0:
        #     raise ValueError("L'immagine fornita non presenta alcun punto di fine.")
        # elif num_caselle_rosse > 1:
        #     raise ValueError("L'immagine fornita non presenta un unico punto di fine.")

    def create_weighted_graph(self):
        # Crea un grafo non diretto vuoto
        G = nx.Graph()

        # Aggiungi tutti i nodi al grafo, con il loro nome dato dalle coordinate
        height = len(self.maze)
        width = len(self.maze[0])
        for i in range(height):
            for j in range(width):
                node_name = f"{i},{j}"
                G.add_node(node_name)

        # Aggiungi gli archi pesati tra i nodi adiacenti
        for i in range(height):
            for j in range(width):
                # Se la cella contiene un muro, passa alla prossima
                if self.maze[i][j] == 0:
                    continue

                # Se non è un muro, crea gli archi con i nodi adiacenti (se esistono)
                node_name = f"{i},{j}"
                if i > 0 and self.maze[i - 1][j] != 0:
                    neighbor_name = f"{i - 1},{j}"
                    weight = self.maze[i - 1][j]
                    G.add_edge(node_name, neighbor_name, weight=weight)
                if i < height - 1 and self.maze[i + 1][j] != 0:
                    neighbor_name = f"{i + 1},{j}"
                    weight = self.maze[i + 1][j]
                    G.add_edge(node_name, neighbor_name, weight=weight)
                if j > 0 and self.maze[i][j - 1] != 0:
                    neighbor_name = f"{i},{j - 1}"
                    weight = self.maze[i][j - 1]
                    G.add_edge(node_name, neighbor_name, weight=weight)
                if j < width - 1 and self.maze[i][j + 1] != 0:
                    neighbor_name = f"{i},{j + 1}"
                    weight = self.maze[i][j + 1]
                    G.add_edge(node_name, neighbor_name, weight=weight)

        return G

    def shortest_path(self) -> List[Tuple[int, int]]:
        G = self.create_weighted_graph()
        shortest_paths = {}
        for start_node in self.start:
            # Calcola il percorso più breve dal nodo di partenza al nodo di arrivo
            end_node = f"{self.end[0]},{self.end[1]}"
            start_node_name = f"{start_node[0]},{start_node[1]}"
            shortest_path = nx.shortest_path(G, start_node_name, end_node, weight='weight')

            # Salva il percorso più breve e il suo costo
            cost = nx.shortest_path_length(G, start_node_name, end_node, weight='weight')
            shortest_paths[start_node] = {'path': shortest_path, 'cost': cost}

        return shortest_paths

    def draw_path(self, path: List[Tuple[int, int]]) -> None:
        if not self.image:
            raise ValueError("Labirinto non creato")

        # crea un oggetto per disegnare sull'immagine
        draw = ImageDraw.Draw(self.image)

        # converte le coordinate del percorso in pixel
        cell_size = 10
        pixel_path = [(j * cell_size + cell_size // 2, i * cell_size + cell_size // 2) for i, j in path]

        # disegna il percorso sull'immagine
        draw.line(pixel_path, fill=(255, 0, 0), width=3)

        # mostra l'immagine
        self.image.show()


labirinto = Labirinto()
# labirinto.gestisci_input("/Users/edoardocaliano/Desktop/Labyrinth/indata/20-10_marked (1).tiff")
labirinto.gestisci_input("/Users/edoardocaliano/Desktop/Labyrinth/indata/20-10_marked (1).tiff")

print(labirinto)





