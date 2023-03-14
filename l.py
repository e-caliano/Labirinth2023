import json
from PIL import Image


class Labirinto:
    def __init__(self):
        self.larghezza = 0
        self.altezza = 0
        self.pareti = []
        self.iniziali = []
        self.finale = None
        self.costi = {}

    def parse_input(input_file):
        if input_file.endswith(".json"):
            with open(input_file) as f:
                data = json.load(f)
            labirinto = Labirinto.from_dict(data)
        elif input_file.endswith((".png", ".jpg", ".jpeg", ".tiff")):
            labirinto = Labirinto.from_image(input_file)
        else:
            raise ValueError("Formato file non supportato.")
        return labirinto

    class Labirinto:
        def __init__(self):
            self.grid = []
            self.width = 0
            self.height = 0

        @classmethod
        def from_dict(cls, data):
            labirinto = cls()
            labirinto.width = data["larghezza"]
            labirinto.height = data["altezza"]
            for riga in data["labirinto"]:
                nuova_riga = []
                for cella in riga:
                    if cella == "X":
                        nuova_riga.append(1)
                    else:
                        nuova_riga.append(0)
                labirinto.grid.append(nuova_riga)
            return labirinto


