from typing import Any

from prompt_toolkit.styles import Style

COLORS: dict[str, str] = {
    "Amber": "#ffc107",
    "Black": "#000000",
    "Blue": "#2196f3",
    "Cyan": "#00bcd4",
    "Deep Orange": "#ff5722",
    "Deep Purple": "#673ab7",
    "Green": "#4caf50",
    "Indigo": "#3f51b5",
    "Light Blue": "#03a9f4",
    "Light Green": "#8bc34a",
    "Lime": "#cddc39",
    "Orange": "#ff9800",
    "Pink": "#e81e63",
    "Purple": "#9c27b0",
    "Red": "#f44336",
    "Teal": "#009688",
    "Yellow": "#ffeb3b",
    "White": "#ffffff",
}

STARTING_VALUES: dict[Any, Any] = {
    "Name": "Jean de Joinville",
    "HP": 100,
    "Silver": 10,
    "Town": "Caerwyn",
    "Country": "Falias",
}

ASCII_MAP_VALUES: dict[Any, Any] = {
    "Width": 50,
    "Height": 20,
    "Symbols": {"Town": "#", "Player": "@", "Background": ".", "Country": "%"},
}

ASCII_STYLES: Style = Style.from_dict(
    {
        "town": COLORS["Purple"],
        "country": COLORS["Pink"],
        "player": COLORS["Blue"],
        "background": COLORS["Light Green"],
        "area-name": COLORS["White"],
        "buy": COLORS["White"],
        "sell": COLORS["White"],
    }
)


NAMES = {
    "femme": [
        "Agatia",
        "Agnese",
        "Agnesina",
        "Alba",
        "Alessandra",
        "Anastasia",
        "Andriana",
        "Angela",
        "Angelica",
        "Anna",
        "Antea",
        "Antonia",
        "Anzola",
        "Barbara",
        "Bella",
        "Benetta",
        "Benvegnuda",
        "Betta",
        "Bettina",
        "Bianca",
        "Borthola",
        "Camilla",
        "Cassandra",
        "Catarina",
        "Cattarina",
        "Cecilia",
        "Chiara",
        "Chiaretta",
        "Christina",
        "Clara",
        "Claudia",
        "Contarina",
        "Cornelia",
        "Corona",
        "Cristina",
        "Daniela",
        "Diana",
        "Dionora",
        "Elena",
        "Elisabetta",
        "Emilia",
        "Eugenia",
        "Faustina",
        "Felicita",
        "Fiametta",
        "Filomena",
        "Fiordelise",
        "Fiorenza",
        "Franceschina",
        "Gabriella",
        "Gaspara",
        "Giulia",
        "Giustina",
        "Gratiosa",
        "Helena",
        "Helia",
        "Hortensa",
        "Iacoma",
        "Isabella",
        "Isabetta",
        "Iseppa",
        "Jacomina",
        "Julia",
        "Justina",
        "Laura",
        "Lavinia",
        "Leandra",
        "Leonarda",
        "Libera",
        "Livia",
        "Lodovica",
        "Lucia",
        "Lucieta",
        "Lugretia",
        "Lugrezia",
        "Madalena",
        "Maddalena",
        "Marcella",
        "Margarita",
        "Margherita",
        "Maria",
        "Marieta",
        "Marietta",
        "Marina",
        "Marita",
        "Matthia",
        "Menega",
        "Meneghina",
        "Moderata",
        "Nicolosa",
        "Oliva",
        "Olivia",
        "Orelia",
        "Orsa",
        "Orseta",
        "Orsetta",
        "Orsolina",
        "Osana",
        "Paola",
        "Paolina",
        "Pasqueta",
        "Paula",
        "Paulina",
        "Pelegrina",
        "Perina",
        "Philippa",
        "Pollonia",
        "Polonia",
        "Portia",
        "Prudentia",
        "Pulisena",
        "Pulissena",
        "Regina",
        "Rosa",
        "Sabina",
        "Samaritana",
        "Santina",
        "Simona",
        "Simonetta",
        "Sofia",
        "Stella",
        "Susanna",
        "Thomasina",
        "Todara",
        "Tomasina",
        "Valentina",
        "Valeria",
        "Vendramina",
        "Veneranda",
        "Veniera",
        "Veronica",
        "Viena",
        "Vienna",
        "Vincenza",
        "Violante",
        "Virginia",
        "Vittoria",
        "Zaneta",
        "Zanetta",
        "Zuanna",
    ],
    "masc": [
        "Agustin",
        "Alexander",
        "Aloysius",
        "Alvise",
        "Ambrogio",
        "Ambrosius",
        "Ambroso",
        "Andrea",
        "Angelo",
        "Annibale",
        "Antonio",
        "Anzolo",
        "Aurelio",
        "Austin",
        "Baldissere",
        "Bartholomio",
        "Bastian",
        "Bastiano",
        "Batista",
        "Battista",
        "Benedetto",
        "Benetto",
        "Bernardin",
        "Bernardo",
        "Biasio",
        "Bortholo",
        "Bortolo",
        "Camillus",
        "Carlo",
        "Claudio",
        "Cristofolo",
        "Dionisio",
        "Domenego",
        "Domenico",
        "Filippo",
        "Francesco",
        "Gabriele",
        "Galeazzo",
        "Gasparo",
        "Giacomo",
        "Giambattista",
        "Gieronimo",
        "Giovanbattista",
        "Giovanni Battista",
        "Giovanni",
        "Girolamo",
        "Giulio",
        "Guglielmo",
        "Hieronimo",
        "Iacomo",
        "Ippolito",
        "Iseppo",
        "Iulio",
        "Jacomo",
        "Jacopo",
        "Lazaro",
        "Lodovico",
        "Lorenzo",
        "Luca",
        "Lundardo",
        "Magno",
        "Marcantonio",
        "Marcello",
        "Marco",
        "Martin",
        "Mercurio",
        "Miro",
        "Nicolo",
        "Paolo",
        "Pasqualin",
        "Paulo",
        "Petro",
        "PierAntonio",
        "Piero",
        "Raffaele",
        "Rocco",
        "Rugir",
        "Salvador",
        "Stefano",
        "Teodor",
        "Tobias",
        "Tomaso",
        "Tommaso",
        "Tranquilo",
        "Valentin",
        "Valerio",
        "Ventura",
        "Venturo",
        "Vincenzo",
        "Vittorio",
        "Vivian",
        "Zacharia",
        "Zago",
        "Zanetto",
        "Zordan",
        "Zorzi",
        "Zuan'Antonio",
        "Zuan",
        "Zuandomenego",
        "Zuane",
        "ZuanGiacomo",
        "Zuann",
        "Zuanne",
    ],
    "occupations": [
        ["Strazzaruola", "second hand clothes dealer"],
        ["Linaruola", "linen maker"],
        ["Fornera", "baker"],
        ["Fruttaruola", "fruit vendor"],
        ["Spiciera", "spice vendor"],
        ["Barcaruola", "boatwoman"],
        ["Zavatera", "cobbler"],
        ["Cassellera", "cobbler"],
        ["Vellera", "sail maker"],
        ["Meretrice", "prostitute"],
        ["Albergatrice", "innkeeper"],
        ["Furlana", "laundress"],
        ["Herbardina", "herb seller"],
    ],
}
