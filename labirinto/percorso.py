from queue import PriorityQueue


class RicercaPercorso:

    """
    Questa classe implementa l'algoritmo di ricerca del percorso più breve in un labirinto utilizzando la coda prioritaria e l'algoritmo A*.
    """
    #Inizializziamo gli attributi labirinto, width e height dell'oggetto RicercaPercorso. width e height sono le dimensioni del labirinto.
    def __init__(self, labirinto):
        """
        Costruttore della classe RicercaPercorso
        :param labirinto: richiamerà la classe Labirinto per utilizzare le informazioni del labirinto, sopratutto la matrice di posizioni

        """
        self.labirinto = labirinto
        self.width = len(self.labirinto.maze[0])
        self.height = len(self.labirinto.maze)

    def trova_percorsi(self):

        """
        Metodo che trova i percorsi con costo minimo da start ad end e utilizzando l'algoritmo A* per trovare il percorso più breve fino alla posizione di arrivo.
        :return: paths : lista dei percorsi, costi_totali : lista dei costi
        """
        #inizializzo due liste vuote dei percorsi e dei costi
        paths = []
        costi_totali = []

        for start_pos in self.labirinto.start:
            # Dizionario per tenere traccia del costo minimo dallo start ad ogni cella
            costo_minimo = {(i, j): float('inf') for i in range(self.height) for j in range(self.width)}
            costo_minimo[start_pos] = 0

            # Dizionario per tenere traccia del percorso migliore
            best_path = {}

            # Coda prioritaria che contiene le celle da esplorare
            queue = PriorityQueue()
            queue.put(start_pos, 0)

            # Viene eseguito un ciclo while fino a quando la coda dei nodi da esplorare non è vuota
            while not queue.empty():
                # Viene prelevato il nodo corrente dalla coda, che rappresenta la posizione corrente del personaggio nel labirinto.
                current_pos = queue.get()

                # Se la posizione corrente corrisponde alla fine del labirinto, viene trovato un percorso valido.
                if current_pos == self.labirinto.end:
                    # Percorso trovato, lo aggiungiamo alla lista dei percorsi
                    path = [current_pos]
                    # Vengono esplorate tutte le celle adiacenti alla posizione corrente e per ogni cella adiacente viene calcolato il costo del percorso dalla posizione corrente alla cella adiacente e la distanza dalla cella adiacente alla fine del labirinto.
                    while current_pos != start_pos:
                        path.insert(0, best_path[current_pos])
                        current_pos = best_path[current_pos]

                    paths.append(path)
                    break

                # La prima riga estrae le coordinate della posizione corrente (current_pos).
                row, col = current_pos
                # La lista neighbors viene inizializzata come lista vuota per contenere le posizioni adiacenti alla posizione corrente.
                neighbors = []
                if row > 0 and self.labirinto.maze[row - 1][col]:
                    neighbors.append((row - 1, col))
                if row < self.height - 1 and self.labirinto.maze[row + 1][col]:
                    neighbors.append((row + 1, col))
                if col > 0 and self.labirinto.maze[row][col - 1]:
                    neighbors.append((row, col - 1))
                if col < self.width - 1 and self.labirinto.maze[row][col + 1]:
                    neighbors.append((row, col + 1))
                # Dopo aver trovato tutte le posizioni adiacenti valide, viene eseguito un ciclo for per tutte le posizioni adiacenti nella lista neighbors.
                for neighbor in neighbors:
                    # Per ogni posizione adiacente, viene calcolato il costo (costo) di spostamento da current_pos a neighbor. Il costo è determinato dal valore della cella nella griglia del labirinto (self.labirinto.maze) nella posizione di neighbor.
                    costo = self.labirinto.maze[neighbor[0]][neighbor[1]]
                    # Successivamente viene calcolata la distanza dal punto di partenza alla posizione neighbor (distanza). Questo viene fatto sommando il costo del percorso minimo dalla posizione di partenza (current_pos) a neighbor, al costo del percorso minimo dalla posizione di partenza al punto finale.
                    distanza = costo_minimo[current_pos] + costo
                    # Se la distanza calcolata per questa posizione adiacente è inferiore al costo minimo precedente per neighbor, allora viene aggiornato il costo minimo per neighbor e la migliore posizione precedente (best_path) viene impostata come current_pos. Infine, la posizione neighbor viene inserita nella coda di priorità (queue) con la sua priorità calcolata come la somma della distanza e della distanza stimata dal punto di partenza al punto finale (self.calcola_distanza).
                    if distanza < costo_minimo[neighbor]:
                        costo_minimo[neighbor] = distanza
                        best_path[neighbor] = current_pos
                        priority = distanza + self.calcola_distanza(neighbor, self.labirinto.end)
                        queue.put(neighbor, priority)

            # Aggiungiamo il costo totale del percorso trovato alla lista dei costi totali
            costi_totali.append(costo_minimo[self.labirinto.end] + self.calcola_lunghezza_percorso(paths[-1]))
        # Alla fine del ciclo, la lista dei percorsi trovati viene restituita insieme alla lista dei costi totali dei percorsi.
        return paths, costi_totali

    def calcola_lunghezza_percorso(self, path):
        """
        Metodo per calcolare la lunghezza totale del percorso in pixel
        :param path: lista di tuple contenenti le coordinate delle celle del percorso
        :return: lunghezza del percorso
        """
        lunghezza = 0
        for i in range(len(path) - 1):
            # Calcoliamo la distanza euclidea tra la cella corrente e quella successiva
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            distanza = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            lunghezza += distanza
        return lunghezza

    def calcola_distanza(self, pos1, pos2):

        """
        Metodo per calcolare la distanza di Manhattan tra due celle del labirinto
        :param pos1: prima cella
        :param pos2: seconda cella
        :return: distanza di Manhattan tra le due celle
        """
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2)



