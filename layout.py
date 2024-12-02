# layout should only export the layout of the map

block_meanings = {
    0: "road",
    1: "wall",
    2: "border"
}

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
].reverse()

# 一格一公尺

gap = [3, 2, 2, 3, 2, 2, 3, 2, 3, 3, 3, 2, 4, 2, 3, 7, 3]

layout_map = []

def generate_map():
    for i in range(1):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(3)
            if(j != len(gap) - 1):
                this_row.append(3)
        this_row.append(3)
        layout_map.append(this_row)

    for i in range(17):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(1)
            if(j != len(gap) - 1):
                this_row.append(0)
        this_row.append(3)
        layout_map.append(this_row)
    for i in range(6):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(0)
            if(j != len(gap) - 1):
                this_row.append(0)
        this_row.append(3)
        layout_map.append(this_row)
    for i in range(2):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(1)
            if(j != len(gap) - 1):
                this_row.append(1)
        this_row.append(3)
        layout_map.append(this_row)

    for i in range(1):
        this_row = []
        this_row.append(3)
        for j in range(len(gap)):
            for k in range(gap[j]):
                this_row.append(3)
            if(j != len(gap) - 1):
                this_row.append(3)
        this_row.append(3)
        layout_map.append(this_row)


def get_map():
    for i in range(len(layout_map)):
        for j in range(len(layout_map[i])):
            if(layout_map[i][j] == 0):
                print(" ", end="")
            else:
                print("#", end="")
        print()

generate_map()
get_map()