from PIL import Image, ImageDraw
import json


class Risultati:
    def __init__(self, labirinto, paths, costo_totale):
        """
        Costruttore della classe risultati che riprende le informazioni dalla classe Labirinto
        :param labirinto: matrice che rappresenta il labrinto
        :param paths: lista dei percorsi con costo minimo per ogni posizione di inizio
        :param costo_totale: lista dei costi dei percorsi in "paths"
        :return:
        """
        self.labirinto = labirinto
        self.width = len(self.labirinto.maze[0])
        self.height = len(self.labirinto.maze)
        self.lista_percorsi = paths
        self.lista_costi = costo_totale
        self.image = self.labirinto.path_image

    def crea_immagine(self, nome_file):
        """
        Metodo per creare un'immagine del labirinto con i percorsi colorati
        :param nome_file: nome del file in cui salvare l'immagine
        """
        # prendo l'immagine
        image = Image.open(self.image)
        # variabile per colorare i percorsi sull'immagine
        draw = ImageDraw.Draw(image)

        # Coloriamo i percorsi trovati in rosso (poichè verranno fatti in file diversi va anche bene utilizzare lo stesso colore)
        colori = ['red']
        for i, path in enumerate(self.lista_percorsi):
            colore = colori[i % len(colori)]
            x, y = path
            #coloro i percorsi
            draw.rectangle((y, x, y, x), fill=colore, width=0)
            if self.labirinto.maze[x][y] == 0:
                draw.rectangle((y, x, y + 1, x + 1), fill='black', width=0.3)
        # Salviamo l'immagine
        image.save(nome_file, optimize=True)


    def crea_file_json(self, nome_file, index):
        """
        Metodo per creare un file JSON con le informazioni sui percorsi
        :param nome_file: nome del file in cui salvare il JSON
        """
        # Creiamo un dizionario contenente le informazioni sui percorsi
        dati = []
        # Il metodo quindi crea un dizionario dati contenente le informazioni relative al percorso selezionato, tra cui la posizione iniziale, la posizione finale, il costo totale del percorso e la lista dei nodi attraversati.
        pos_iniziale = self.labirinto.start[index]
        pos_finale = self.labirinto.end
        costo = self.lista_costi[index]
        dati.append({'pos_iniziale': pos_iniziale, 'pos_finale': pos_finale, 'costo': costo, 'path': self.lista_percorsi})

        # Scriviamo il dizionario su file JSON
        with open(nome_file, 'w') as f:
            json.dump(dati, f, indent=4)