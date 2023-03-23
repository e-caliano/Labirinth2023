import os
from PIL import Image
import json


class Labirinto:
    """
    costruttore della classe labirinto
    """
    def __init__(self, percorso_file=None):
        # impostazione della directory "indata" che contiene i casi di test
        self.percorso_file = percorso_file
        self.data_dir = os.path.join(os.path.dirname(__file__), 'indata')
        # matrice che ospiterà il labirinto
        self.maze = []
        # matrice che ospiterà i punti di partena
        self.start = []
        # tupla che ospita il punto di arrivo
        self.end = ()
        # immagine che conterrà l'immagine del labirinto
        self.image = None

        if self.percorso_file is not None:
            self.file_path = os.path.join(self.data_dir, self.percorso_file)
        else:
            self.file_path = None


    def gestisci_input(self):
        """
        metodo per il parsing dell'input: se il file è .json allora dovrò chiamare una funzione che dal json mi crea una istanza del labirinto,
        se il file è di tipo immagine allora dovrò chiamare un metodo che crea un'istanza del labirinto a partire dall'immagine.
        :return: none
        """
        if self.file_path is None:
            raise ValueError("File name not specified")

        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        # estrae il nome del file e l'estensione
        estensione = self.percorso_file.split(".")[-1].lower()

        # controllo l'estensione ed eseguo l'azione appropriata
        if estensione == 'json':
            # carico il labirinto dal file JSON
            with open(self.file_path) as json_file:
                data = json.load(json_file)
            self.labirinto_from_json(data)
        # controllo che l'estensione sia di tipo TIFF, JPEG O PNG
        elif estensione in ['tiff', 'jpeg', 'png']:
            # carico il labirinto dall'immagine
            self.image = Image.open(self.file_path)
            self.labirinto_from_image()
        # in tutti gli altri casi non devo supportare l'estensione
        else:
            # gestione dell'errore se l'estensione non è supportata
            print("Estensione del file non supportata")

        return self.maze, self.file_path, self.start, self.end


    def labirinto_from_json(self, data):
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

        self.json_to_image()
        print(self.maze)