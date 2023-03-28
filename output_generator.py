from PIL import Image, ImageDraw


def traccia_percorsi_labirinto(immagine_labirinto, lista_percorsi):
    """

    :param immagine_labirinto: immagine del labirinto
    :param lista_percorsi: lista contenente i percorsi che risolvono il labirinto
    :return: None
    """
    # Apriamo l'immagine del labirinto
    img = Image.open(immagine_labirinto)

    # Creiamo un oggetto "ImageDraw" per disegnare sulle immagini
    draw = ImageDraw.Draw(img)

    # Definiamo i colori dei percorsi
    colori = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']

    # Disegniamo i percorsi sull'immagine
    for i, percorso in enumerate(lista_percorsi):
        colore = colori[i % len(colori)]
        for j in range(len(percorso) - 1):
            x1, y1 = percorso[j]
            x2, y2 = percorso[j + 1]
            draw.line((x1, y1, x2, y2), fill=colore, width=3)

    # Mostraimo l'immagine risultante
    img.show()
