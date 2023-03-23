import os
from PIL import Image
import json


class Labirinto:
    """
    costruttore della classe labirinto
    """
    def __init__(self):
        # matrice che ospiterà il labirinto
        self.maze = []
        # matrice che ospiterà i punti di partena
        self.start = []
        # tupla che ospita il punto di arrivo
        self.end = ()
        # immagine che conterrà l'immagine del labirinto
        self.image = None


    def gestisci_input(self, percorso_file):
        """
        metodo per il parsing dell'input: se il file è .json allora dovrò chiamare una funzione che dal json mi crea una istanza del labirinto,
        se il file è di tipo immagine allora dovrò chiamare un metodo che crea un'istanza del labirinto a partire dall'immagine.
        :return: none
        """
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


    def load_from_json(self, data):
        """
        metodo per creare istanza del labirinto a partire dal file json di input
        :return: labirinto
        """
        # controllo che il JSON abbia i campi prestabiliti
        if set(list(data.keys())) != {"larghezza", "altezza", "pareti", "iniziali", "finale", "costi"}:
            raise ValueError("Struttura file JSON non supportata")
        # popolo la matrice che ospita il labirinto
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


    def load_from_image(self):
        """
        metodo per creare istanza del labirinto a partire dall'immagine di input
        :return: labirinto
        """
        pass


    def maze_to_image(self):
        """
        metodo per creare l'immagine del labirinto a partire dal caricamento del labirinto fornito dal JSON
        :return:
        """
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

