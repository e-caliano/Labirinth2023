import os
from PIL import Image
import json
from pathlib import Path


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
        Metodo per il parsing dell'input: se il file è .json allora dovrò chiamare una funzione che dal json mi crea una istanza del labirinto,
        se il file è di tipo immagine allora dovrò chiamare un metodo che crea un'istanza del labirinto a partire dall'immagine.
        :return: self.maze : labirinto in matrice, self.file_path : path di riferimento, self.path_image : path dell'immagine, self.start : lista delle posizioni iniziali, self.end : posizione finale
        """
        # check sull'input del file
        if self.file_path is None:
            raise ValueError("File name non specificato")
        # se il file non esiste, sollecito un errore
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File non trovato: {self.file_path}")
        # estrae il nome del file e l'estensione
        estensione = self.percorso_file.split(".")[-1].lower()

        # controllo l'estensione ed eseguo l'azione appropriata
        if estensione == 'json':
            # carico il labirinto dal file JSON
            with open(self.file_path) as json_file:
                data = json.load(json_file)
            # chiamo la funzione che elabora il JSON per creare il labrinto e manipolarlo
            self.labirinto_from_json(data)
            # salvo il path nella variabile name
            name = Path(self.file_path).name
            # estrapolo solo il nome dal path in input e lo salvo dentro name
            name = os.path.splitext(name)[0]
            # salvo l'immagine del labirinto nella cartella json_image
            self.path_image = './labirinto/json_image/' + name + '.png'
            self.image.save(self.path_image)
        # controllo che l'estensione sia di tipo TIFF, JPEG O PNG
        elif estensione in ['tiff', 'jpeg', 'png']:
            # carico il labirinto dall'immagine
            self.path_image = self.file_path
            self.image = Image.open(self.file_path)
            self.labirinto_from_image()
        # in tutti gli altri casi non devo supportare l'estensione
        else:
            # gestione dell'errore se l'estensione non è supportata
            print("Estensione del file non supportata")

        return self.maze, self.file_path, self.path_image, self.start, self.end

    def labirinto_from_json(self, data):
        """
        metodo per creare istanza del labirinto a partire dal file json di input
        :return:
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


    def json_to_image(self):
        """
        Metodo per restituire un'immagine a partire dal file json in ingresso
        :return:
        """
        # creazione di un'immagine vuota tramite Image, che abbia dimensione pari alla matrice che contiene il labirinto
        self.image = Image.new("RGB", (len(self.maze[0]), len(self.maze)))
        pixels = self.image.load()
        # Impostazione dei pixel dell'immagine in base alla matrice del labirinto
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 0:
                    # imposto il muro inizializzato a 0
                    pixels[j, i] = (0, 0, 0)  # muro = nero
                    # imposto il cammino inizializzato a 1
                elif self.maze[i][j] == 1:
                    pixels[j, i] = (255, 255, 255)  # cammino = bianco
                else:
                    # imposto il cammino pesato
                    pixels[j, i] = ((self.maze[i][j] - 1) * 16, (self.maze[i][j] - 1) * 16, (self.maze[i][j] - 1) * 16)  # cammino pesato = grigio scuro
        # imposto l'inizio e la fine del labirinto
        i = self.end[0]
        j = self.end[1]
        pixels[j, i] = (255, 0, 0)  # arrivo = rosso
        for st in self.start:
            i = st[0]
            j = st[1]
            pixels[j, i] = (0, 255, 0)  # partenza = verde


    def labirinto_from_image(self):
        """
        Metodo che, dall'immagine, fornita nei diversi formati TIFF, JPEG o PNG, restituisce la matrice del labirinto
        :return:
        """
        # apre l'immagine e ottiene i dati dei pixel
        pixel = self.image.load()
        larghezza, altezza = self.image.size

        # inizializza la matrice del labirinto
        labirinto = []
        for i in range(altezza):
            labirinto.append([0] * larghezza)

        # analizzo i pixel dell'immagine e costruisco la matrice del labirinto
        for y in range(altezza):
            for x in range(larghezza):
                r, g, b = pixel[x, y]
                # se ii pixel sono verdi rappresentano l'inizio, attraversabile =1
                if r == 0 and g == 255 and b == 0:
                    self.start.append((y, x))
                    labirinto[y][x] = 1
                # se il pixel è rosso è la fine, attraversabile = 1
                elif r == 255 and g == 0 and b == 0:
                    self.end = (y, x)
                    labirinto[y][x] = 1
                # pixel nero = muro = 0
                elif r == 0 and g == 0 and b == 0:
                    labirinto[y][x] = 0
                # pixel bianco = posizione attraversabile = 1
                elif r == 255 and g == 255 and b == 255:
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
                    labirinto[y][x] = costo + 1  # associazione del costo in base al grigio, assumento che il grigio sia anche un corridoio
        self.maze = labirinto