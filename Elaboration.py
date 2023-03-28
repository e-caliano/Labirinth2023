from labirinto import Labirinto
from percorso import RicercaPercorso
from risultatoLabirinto import Risultati

def risoluzioneLabirinto():
    """
    Metodo utile per richiamare le varie classi e gestire gli output
    :return:
    """
    #Chiedo all'utente di inserire il nome del file presente nella cartella indata
    file=input('Inserisci nome del file con la sua estensione: ')
    #richiamo le varie funzioni in base ai parametri richiesti
    labirinto = Labirinto(file)
    labirinto.gestisci_input()
    rp = RicercaPercorso(labirinto)
    #creo una cartella per gli output
    outputDir = "output/"

    #ottengo la lista dei percorsi per il file scelto e la lista dei costi totali
    paths, costo_totale = rp.trova_percorsi()

    #per ogni percorso creerò i file dei risultati e li inserisco nella cartella degli output
    for i, percorsi in enumerate(paths):
        risultati = Risultati(labirinto, percorsi, costo_totale)
        index = i
        #Se il percorso ha costo 'inf' mostro che non è stato trovato nessun percorso
        if costo_totale[i] == float('inf'):
            index = i+1
            print('Non è stato trovato nessun percorso per il percorso numero: {0}'.format(index))

        # crea l'immagine e il file JSON
        risultati.crea_immagine(outputDir + 'Risultati-{0}.png'.format(i))
        risultati.crea_file_json(outputDir + 'Risultati-{0}.json'.format(i), index)