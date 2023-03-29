# Labyrinth2023
Progetto finale del corso 'Programmazione' 2022-2023

## Traccia del progetto
Il programma deve acquisire il layout di un labirinto costituito da una matrice di posizioni, una o più posizioni di partenza e una posizione di arrivo, e determinare per ogni punto di partenza il percorso che permette di raggiungere il punto di arrivo o, in alternativa, se non esiste alcun percorso possibile.

Nel labirinto sono presenti posizioni a cui è associato un costo. Nel caso esista un percorso che permette di raggiungere da un punto di partenza il punto di arrivo, oltre al percorso, il programma deve anche fornire il suo costo totale che è la somma dei costi incontrati lungo di esso più la lunghezza del percorso in pixel. Nel caso esistano più percorsi possibili da un determinato punto di partenza, il programma deve fornire il percorso con il costo minore.

Il labirinto e i punti di partenza e di arrivo possono essere forniti attraverso un file in formato JSON o un'immagine. Di seguito, per ogni formato possibile, viene fornita la specifica delle convenzioni usate per rappresentare il layout del labirinto, le posizioni a cui è associato un punteggio, e le posizioni di partenza e di arrivo.

Il risultato finale deve essere fornito attraverso:

un'immagine su cui è indicato il percorso con un colore diverso per ogni punto di partenza;

un file JSON associato all'immagine con l'informazione del punteggio raggiunto da ogni percorso o, in alternativa, da un messaggio nel caso non esista un percorso possibile da qualcuno delle posizioni di partenza.

# Labirinto fornito come file JSON
Il file è un dizionario con le seguenti chiavi:

"larghezza": un numero che indica il numero di posizioni lungo la dimensione orizzontale;
"altezza": un numero che indica il numero di posizioni lungo la dimensione verticale;
"pareti": una lista di segmenti, ogni segmento costituito da un dizionario con chiavi:
"orientamento": "H" per orizzontale, "V" per verticale;
"posizione": un coppia di indici che indicano una posizione "iniziale" (per convenzione il segmento si estende in orizzontale da sinistra verso destra e in verticale dall'alto verso il basso);
"lunghezza": un numero che indica il numero di posizioni occupate dal segmento;
"iniziali": una lista di coppie di indici che indicano ciascuno una posizione di partenza;
"finale": una coppia di indici che indica la posizione di arrivo;
"costi": una lista di posizioni con costo, che sono triple costituite da una coppia di indici che indicano una posizione e un valore intero da 1 a 15 che indica il costo.

# Labirinto fornito come immagine
L'immagine è un'immagine a colori in formato TIFF, PNG o JPEG che corrisponde a una matrice rettangolare un cui i pixel neri corrispondono a posizioni occupate da pareti che non possono essere attraversate, e tutti gli altri pixel corrispondono a posizioni che possono essere attraversate per raggiungere il punto di arrivo.

I pixel bianchi sono posizioni che non assegnano punti, i pixel grigi indicano caselle che assegnano costi, i pixel verdi indicano le posizioni di partenza, il pixel rosso indica la posizione di arrivo.

I livelli di grigio possibili sono:

16 che assegna un costo pari a 1
32 che assegna un costo pari a 2
48 che assegna un costo pari a 3
64 che assegna un costo pari a 4
80 che assegna un costo pari a 5
96 che assegna un costo pari a 6
112 che assegna un costo pari a 7
128 che assegna un costo pari a 8
144 che assegna un costo pari a 9
160 che assegna un costo pari a 10
176 che assegna un costo pari a 11
192 che assegna un costo pari a 12
208 che assegna un costo pari a 13
124 che assegna un costo pari a 14
240 che assegna un costo pari a 15

# Utilizzo del progetto
Per il corretto funzionamento del programma, è necessario scaricare l'intera cartella 'labirinto', all'interno della quale si trovano i diversi file fondamentali per avviare il progetto.
Per ottenere i vari risultati è necessario effettuare il RUN del file main.py e verrà richiesto di inserire il nome del file, già presente nella cartella ‘indata’.
Nel caso in cui il labirinto del file scelto abbia almeno un percorso non possibile, nell’output verrà definita la presenza di questo percorso e il rispettivo indice.
Il RUN del programma prevede la creazione automatica di una cartella ‘output’ in cui vengono creati i vari file json e immagine ottenuti (per ogni percorso possibile verranno creati un file json ed un file immagine).
I file json conterranno informazioni riguardo la posizione iniziale, finale, costo del percorso e il percorso totale.
I file immagine conterranno invece il labirinto con il percorso disegnato dalla posizione iniziale alla posizione finale.
Nel caso di scelta in ingresso di un file json, il file prevede una creazione automatica di una cartella ‘json_image’, in cui verranno salvate le varie immagini del labirinto nella forma precedente al momento in cui verrà disegnato.

# Esempio di prova di test
## Esempio Input del nostro progetto
Una volta avviato il codice del 'main' viene chiesto di inserire il inserire il file json o immagine.

```
Inserisci nome del file con la sua estensione:
```

Bisognerà inserire il nome del file presente nella cartella 'indata'

```
30-20_marked.json
```
Abbiamo scelto in questo caso il file '30-20_marked.json'.
Verranno restituiti i seguenti risultati: due file json e due file immagini dei percorsi.

## Esempio di Output del nostro progetto
### Primo percorso:
- Risultati-0.png

![image](https://user-images.githubusercontent.com/122620191/228555285-88a0fafb-62d9-40f5-accd-f420385048e5.png)             


- Risultati-0.json
 
```
[
    {
        "pos_iniziale": [
            0,
            29
        ],
        "pos_finale": [
            21,
            31
        ],
        "costo": 126.0,
        "path": [
            [
                0,
                29
            ],
            [
                1,
                29
            ],
            [
                1,
                28
            ],
            [
                1,
                27
        ...
```


### Secondo percorso:
- Risultati-1.png

![image](https://user-images.githubusercontent.com/122620191/228555501-0fbd7352-4141-4caa-b984-09f267fe4e76.png)             


- Risultati-1.json

```
[
    {
        "pos_iniziale": [
            19,
            60
        ],
        "pos_finale": [
            21,
            31
        ],
        "costo": 454.0,
        "path": [
            [
                19,
                60
            ],
            [
                19,
                59
            ],
            [
                18,
                59
            ],
            [
                17,
                59
            ],
           ...
```






