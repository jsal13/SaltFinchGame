from saltfinchgame.constants import ASCII_MAP_VALUES
from saltfinchgame.data_structures.ascii_map import MapASCII

map_ascii = MapASCII(
    height=ASCII_MAP_VALUES["Height"],
    width=ASCII_MAP_VALUES["Width"],
    symbols=ASCII_MAP_VALUES["Symbols"],
)

if __name__ == "__main__":
    print(map_ascii)
