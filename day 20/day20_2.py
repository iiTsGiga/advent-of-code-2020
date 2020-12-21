# creates each possible borders for the tile
# "#" is translated to 1 and "." to 0
# the borders then gets translated from binary into an integer (easier to debug and better in performance when comparing edges)
def createBorders(tile):
    return [
        int("".join(tile[0][i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),       # top
        int("".join(tile[0][9 - i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),   # top flipped
        int("".join(tile[-1][i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),      # bottom
        int("".join(tile[-1][9 - i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),  # bottom flipped
        int("".join(tile[i][0] for i in range(10)).replace(".", "0").replace("#", "1"), 2),       # left
        int("".join(tile[9 - i][0] for i in range(10)).replace(".", "0").replace("#", "1"), 2),   # left flipped
        int("".join(tile[i][-1] for i in range(10)).replace(".", "0").replace("#", "1"), 2),      # right
        int("".join(tile[9 - i][-1] for i in range(10)).replace(".", "0").replace("#", "1"), 2)   # right flipped
    ]

# len(neighbors[id]) must be equal to 1 which is the tile's right neighbour
def buildRight(x, y):
    if x == N - 1 or y == N - 1:  # if we reached one of the edges
        return
    if y == 0:
        img[y][x+1] = neighbours[img[y][x]].pop()  # set the right neighbour (only in the first row) and remove the right neighbour from this tile's neighbours
        neighbours[img[y][x+1]].remove(img[y][x])  # remove this tile from the right neighbour's neighbours
    # search for the tile which is on the bottom right of this tile
    for id1 in neighbours[img[y][x+1]]:
        for id2 in neighbours[img[y+1][x]]:
            if id1 == id2:
                img[y+1][x+1] = id1
                neighbours[img[y][x+1]].remove(id1)  # remove diagonal neighbour from right's neighbours
                neighbours[id1].remove(img[y][x+1])  # remove right neighbour from diagonal's neighbours
                neighbours[img[y+1][x]].remove(id1)  # remove diagonal neighbour from beneath's neighbours
                neighbours[id1].remove(img[y+1][x])  # remove beneath neighbour from diagonal's neighbours
                buildRight(x + 1, y)  # keep building to the right
                return

def matchesRight(x, y):
    return ''.join(img[y][x][i][-1] for i in range(10)) == ''.join(img[y][x+1][i][0] for i in range(10))

def rotateTile(x, y):  # clockwise rotation
    img[y][x] = [''.join(img[y][x][9-j][i] for j in range(10)) for i in range(10)]

def flipTile(x, y):  # flip x
    img[y][x] = [img[y][x][i][::-1] for i in range(10)]

def rotateRow(y):
    for x in range(0, N-1):
        for _ in range(2):
            for _ in range(4):
                if matchesRight(x, y):
                    break
                rotateTile(x + 1, y)
            else:
                flipTile(x + 1, y)
                continue
            break


# -------------- main --------------

# read input:
inp = "".join(line for line in open("day20_input.txt").readlines()).split("\n\n")  # split tiles
tiles = dict()
orig_tiles = dict()
for tile in inp:
    id, capture = tile.split(":\n")  # split tiles into id and tile
    id = int(id.split()[1])
    capture = capture.split("\n")
    tiles[id] = createBorders(capture)  # create all existing borders for the tile
    orig_tiles[id] = capture

# find neighbours:
neighbours = {id: set() for id in tiles}  # keep track of each tile's neighbours
# look for neighbours, if any of the edges in two tiles match, they are neighbours
for id1 in tiles:
    for id2 in tiles:
        if id1 == id2:
            continue
        for b1 in tiles[id1]:
            for b2 in tiles[id2]:
                if b1 == b2:
                    neighbours[id1].add(id2)
                    neighbours[id2].add(id1)

# align:
N = int(len(tiles)**0.5)
img = [[0 for _ in range(N)] for _ in range(N)]
img[0][0] = [id for id in tiles if len(neighbours[id]) == 2][0]  # tiles with 2 neighbours are corners

# align from the top left corner to the bottom right corner
# this goes through each row except for the last
# each row is build by determining the diagonal (bottom right) neighbours of each tile in the row
# only in the first row the right neighbours also get set
# afterwards the right neighbours are already set from the previous run
for i in range(1, N):
    img[i][0] = neighbours[img[i-1][0]].pop()  # at the start it doesn't matter which neighbor is used since the image can still be rotated and flipped afterwards
    neighbours[img[i][0]].remove(img[i-1][0])  #
    buildRight(0, i-1)

# rotate:
img = [[orig_tiles[id] for id in row] for row in img]  # use the string tiles instead of integers (easier to debug)

# get the rotation of the starting corner by matching it with the tiles at (0|0) and (0|1)
# -- all the else-continue-brake-stuff wouldn't be necessary if python had labels to break outer loops
# -- its the same as if I would've put it into a method and used a return in the inner most break, but since this part is only done once, I didn't want to put it into a function
for _ in range(2):
    for _ in range(2):
        for _ in range(2):
            for _ in range(4):
                for _ in range(4):
                    for _ in range(4):
                        if img[0][0][-1] == img[1][0][0] and matchesRight(0, 0):
                            break
                        rotateTile(0, 0)
                    else:
                        rotateTile(0, 1)
                        continue
                    break
                else:
                    rotateTile(1, 0)
                    continue
                break
            else:
                flipTile(0, 0)
                continue
            break
        else:
            flipTile(0, 1)
            continue
        break
    else:
        flipTile(1, 0)
        continue
    break

# first rotate the first tile in the row so it matches the tile above it
# then rotate the whole row correctly
for i in range(N):
    if i > 1:  # skip the first two because they just got rotated correctly
        for _ in range(2):
            for _ in range(4):
                if img[i][0][0] == img[i-1][0][-1]:
                    break
                rotateTile(0, i)
            else:
                flipTile(0, i)
                continue
            break
    rotateRow(i)

# remove borders
for y in range(N):
    for x in range(N):
        img[x][y] = [line[1:-1] for line in img[x][y][1:-1]]

# create final image
new_img = ""
for row in img:
    for y in range(8):
        for tile in row:
            for x in range(8):
                new_img += tile[y][x]
        new_img += "\n"
img = new_img.strip().split("\n")

# search for monsters
monster = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
counter = 0
while True:
    found = False
    for y in range(len(img)-3):
        for x in range(len(img[0])-20):
            for xoff, yoff in monster:
                if img[y+yoff][x+xoff] != "#":
                    break
            else:
                found = True
                for xoff, yoff in monster:
                    img[y+yoff] = img[y+yoff][:x+xoff] + "O" + img[y+yoff][x+xoff+1:]
    if found:
        break
    img = [''.join(img[-1-j][i] for j in range(len(img))) for i in range(len(img))]
    counter += 1
    if counter == 4:
        img = [img[i][::-1] for i in range(len(img))]

# count remaining #-es
counter = 0
for row in img:
    counter += row.count("#")
print(counter)