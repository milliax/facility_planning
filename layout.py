# layout should only export the layout of the map
FROM_TO_CHART = {
    "A": {"B": 0.99, "D": 0.51, "J": 0.26, "K": 0.06},
    "B": {"B": 1.14, "C": 0.68, "D": 0.27, "G": 0.01, "H": 0.48, "J": 0.03, "N": 0.51},
    "C": {
        "A": 0.12,
        "B": 0.03,
        "C": 1.42,
        "D": 1.62,
        "E": 2.16,
        "F": 0.21,
        "G": 0.05,
        "H": 1.65,
        "N": 0.63,
    },
    "D": {
        "B": 0.21,
        "C": 1.04,
        "D": 0.78,
        "E": 0.45,
        "F": 0.06,
        "G": 0.01,
        "H": 0.48,
        "J": 0.73,
        "K": 0.24,
        "M": 0.09,
    },
    "E": {
        "C": 0.07,
        "D": 0.57,
        "E": 0.06,
        "G": 0.04,
        "H": 1.32,
        "J": 0.05,
        "K": 0.36,
        "L": 0.09,
    },
    # Add other rows similarly...
}

LAYOUT_MAP = [[]]

block_meanings = {0: "road", 1: "wall", 2: "border"}

ROWS = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
][::-1]

# 一格一公尺
gap = [3, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 2, 4, 2, 3, 7, 3]

layout_map = []


def generate_map():
    global layout_map
    internal_map = []

    for i in range(3):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(3)
            if j != len(gap) - 1:
                this_row.append(3)
        this_row.append(3)
        internal_map.append(this_row)

    for i in range(17):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(1)
            if j != len(gap) - 1:
                this_row.append(0)
        this_row.append(3)
        internal_map.append(this_row)
    for i in range(6):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(0)
            if j != len(gap) - 1:
                this_row.append(0)
        this_row.append(3)
        internal_map.append(this_row)
    for i in range(2):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(1)
            if j != len(gap) - 1:
                this_row.append(1)
        this_row.append(3)
        internal_map.append(this_row)

    for i in range(1):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(3)
            if j != len(gap) - 1:
                this_row.append(3)
        this_row.append(3)
        internal_map.append(this_row)
    layout_map = internal_map


def get_map():
    for i in range(len(layout_map)):
        for j in range(len(layout_map[i])):
            if layout_map[i][j] == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print()


generate_map()
get_map()
