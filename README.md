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
indata/30-20_marked.json
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

# Dockerfile
Docker può creare immagini automaticamente leggendo le istruzioni da un file Dockerfile. 
Il Dockerfile un documento di testo che contiene tutti i comandi che un utente potrebbe chiamare sulla riga di comando per assemblare un'immagine.
Il Dockerfile che creiamo, contiene tutte le informazioni necessarie alla creazione dell'immagine Docker. Dallo sviluppo dell'ambiente virtuale python, con l'utilizzo del file 'requirements.txt' contenente vari pacchetti e copiando i file presenti nel progetto.
Il modello seguito è: Dockerfile > Docker image > Docker container.

## Immagine Docker
Per prima cosa, bisogna controllare che nella stessa posizione siano presenti i file 'requirements.txt' e 'Dockerfile' (creato in base a ciò detto precedentemente).
Il comando che prevede la creazione dell'immagine è questo:
```
docker build . -t utente/mymaze:1
```
In questo comando:
- __dockerbuild__ avvia il processo di costruzione dell'immagine Docker;
- __.__ specifica la directory corrente come contesto di build, cioè la directory in cui cercare il Dockerfile;
- __nome_utente/nome_immagine:versione__ è il modello. Nel nostro caso: 'utente' rappresenta il nome dell'utente Docker Hub, 'mymaze' rappresenta il nome dell'immagine e '1' rappresenta la versione dell'immagine-

In questo modo, l'immagine Docker verrà creata e assegnata al tag utente/mymaze:1, che può essere utilizzato successivamente per eseguire o distribuire l'immagine.

# Esecuzione del container Docker
Innanzitutto, per poter eseguire il container Docker, c'è bisogno innanzitutto che nel Dockerfile sia presente questo comando:
```
CMD ["python", "./main.py"]
```
E' successivamente necessario eseguire il container Docker specificando i percorsi della cartella 'indata' e della cartella 'output', per poter capire il posizionamento dei dati in ingresso e in uscita.
Il comando da eseguire successivamente è:
```
docker container run -a stdin -a stdout -it -v $(pwd)/labirinto/indata:/usr/src/app/indata -v $(pwd)/labirinto/output:/usr/src/app/output --name labirinto utente/mymaze:1
```
Questo comando avvia un nuovo container Docker a partire da un'immagine Docker denominata "utente/mymaze:1". Il nuovo container viene denominato "labirinto".

- __-a stdin__ e -__a stdout__: questi flag permettono di connettere lo stdin e lo stdout del container con quelli dell'host;
- __-it__: questo flag attiva la modalità interattiva del container, che consente all'utente di interagire con la shell del container;
- __-v $(pwd)/labirinto/indata:/usr/src/app/indata__: questo flag monta la directory indata dell'host all'interno del container, in modo che il container possa accedere ai file in essa contenuti;
- __-v $(pwd)/labirinto/output:/usr/src/app/output__: questo flag monta la directory output dell'host all'interno del container, in modo che il container possa scrivere i file di output generati durante l'esecuzione;
- __--name labirinto__: questo flag assegna un nome al container avviato.

## Cosa succede successivamente?
Se tutto è stato fatto nel modo definito, il comando prededente restituirà il commento:
```
Inserisci nome del file con la sua estensione:
```
Andrà utilizzato il path virutale da analizzare, in quanto utilizziamo il container Docker.
Quindi andrà inserito, nel nostro caso, questo comando:
```
/usr/src/app/indata/30-20_marked.json
```
Ovviamente, si può anche continuare ad eseguire all'interno del container utilizzato, tramite apposito comando:
```
docker container start -ai labirinto
```
Questo comando avvia un container Docker con il nome "labirinto" e fa partire il processo ad esso associato. La flag "-ai" sta per "attach" e "interactive", il che significa che si collega al terminale del container e permette all'utente di interagire con esso attraverso il terminale del proprio sistema operativo.

La parte dedicata alla visualizzazione dell'output,  prevede l'utilizzo di questi comandi:
```
docker start labirinto
docker exec -it labirinto /bin/bash
```
Il primo comando, __docker start labirinto__ avvia il container Docker chiamato "labirinto", se questo container era stato precedentemente arrestato.
Il secondo comando __docker exec -it labirinto /bin/bash__ esegue una shell Bash all'interno del container "labirinto". Questo permette di interagire con il container in modo interattivo, ad esempio per eseguire comandi all'interno del container o per modificare i file al suo interno.
