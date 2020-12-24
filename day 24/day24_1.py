def executeFlip(flip: str):
    i = 0
    x, y = 0, 0
    while i < len(flip):
        posChange = dirCalc[flip[i:i + 1 + (flip[i] in "sn")]]
        x, y = x+posChange[0], y+posChange[1]
        i += 1 + (flip[i] in "sn")
    tiles[x, y] = True if (x, y) not in tiles else not tiles[x, y]

dirCalc = {"w": (-2, 0), "e": (2, 0), "ne": (1, -1), "nw": (-1, -1), "se": (1, 1), "sw": (-1, 1)}  # change in coordinates
tiles = {(0, 0): False}  # False = White, True = Black
for flip in open("day24_input.txt").read().split("\n"):
    executeFlip(flip)
print(list(tiles.values()).count(True))