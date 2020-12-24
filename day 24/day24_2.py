def getPos(pos: tuple, dir: str):
    return pos[0] + dirCalc[dir][0], pos[1] + dirCalc[dir][1]

def getNeighbours(pos: tuple) -> list:
    return [getPos(pos, "w"), getPos(pos, "e"), getPos(pos, "nw"), getPos(pos, "sw"), getPos(pos, "ne"), getPos(pos, "se")]

def fill():
    newTiles = dict()
    for pos in tiles:
        for n in tilesNeighbours[pos]:
            if n not in tiles:
                newTiles[n] = False
                tilesNeighbours[n] = getNeighbours(n)
    tiles.update(newTiles)

def gameOfLife():
    fill()
    newTiles = dict()
    for pos in tiles:
        countBlack = 0
        for n in tilesNeighbours[pos]:
            if n in tiles and tiles[n]:
                countBlack += 1
        if tiles[pos] and (countBlack == 0 or countBlack > 2):
            newTiles[pos] = False
        elif not tiles[pos] and countBlack == 2:
            newTiles[pos] = True
        else:
            newTiles[pos] = tiles[pos]
    tiles.update(newTiles)

def executeFlip(flip: str):
    i = 0
    x, y = 0, 0
    while i < len(flip):
        posChange = dirCalc[flip[i:i + 1 + (flip[i] in "sn")]]
        x, y = x+posChange[0], y+posChange[1]
        i += 1 + (flip[i] in "sn")
    tiles[x, y] = True if (x, y) not in tiles else not tiles[x, y]

dirCalc = {"w": (-2, 0), "e": (2, 0), "ne": (1, -1), "nw": (-1, -1), "se": (1, 1), "sw": (-1, 1)}  # change in coordinates
tilesNeighbours = dict()
tiles = {(0, 0): False}  # False = White, True = Black
for flip in open("day24_input.txt").read().split("\n"):
    executeFlip(flip)
for pos in tiles:
    tilesNeighbours[pos] = getNeighbours(pos)
for _ in range(100):
    gameOfLife()
print(list(tiles.values()).count(True))