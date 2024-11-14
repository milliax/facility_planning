""" Define the layout chart """
WIDTH = 5
HEIGHT = 3
BAND_HEIGHT = 3
AREA_REQUIRED = {
    "A": 10,
    "B": 5,
}
TAG_NAMES = ["A","B"]
FROM_TO_CHART = [
    [0,1],
    [1,0],
]
DISTANCE_CONFIG = "Euclidean" # "Manhattan"
occupation_dist = {}
# occupation_dist = {
#     "A": [square],
#     "B": 0,
# }
# square = {
#     "TL": points,
#     "TR": points,
#     "BL": points,
#     "BR": points,
# }
# points = {
#     "x": 0,
#     "y": 0,
# }

""" Find the middle point of the part """

def find_middle_point(tag: str):
    if(not(tag in TAG_NAMES)):
        # find the square
        raise Exception("The tag is not in the TAG_NAMES")
    
    squares = occupation_dist[tag]

    accumulated_x = []
    accumulated_y = []

    for square in squares:
        accumulated_x.append(square["TL"]["x"] + square["TR"]["x"] + square["BL"]["x"] + square["BR"]["x"])
        accumulated_y.append(square["TL"]["y"] + square["TR"]["y"] + square["BL"]["y"] + square["BR"]["y"])
    
    return {"x": sum(accumulated_x) / len(accumulated_x),"y":sum(accumulated_y) / len(accumulated_y)}

""" Examination Part """

def target_value():
    # get the flow chart 
    value = 0

    for a in range(len(TAG_NAMES)):
        for b in range(len(TAG_NAMES)):
            if (a == b):
                continue
        
            # get from a to b from flow chart
            weight = FROM_TO_CHART[a][b]
            # get the area of a and b
            mid_a = find_middle_point(TAG_NAMES[a])
            mid_b = find_middle_point(TAG_NAMES[b])

            # calculate the distance between a and b euclidean distance
            distance = 0
            if(DISTANCE_CONFIG == "Euclidean"):
                distance = ((mid_a["x"] - mid_b["x"])**2 + (mid_a["y"] - mid_b["y"])**2)**0.5
            else:
                # Manhattan distance
                distance = abs(mid_a["x"] - mid_b["x"]) + abs(mid_a["y"] - mid_b["y"])

            value += weight * distance
    
    return value

""" MAIN Program """

