def createBorders(tile):
    return [
        int("".join(tile[0][i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[0][9 - i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[-1][i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[-1][9 - i] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[i][0] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[9 - i][0] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[i][-1] for i in range(10)).replace(".", "0").replace("#", "1"), 2),
        int("".join(tile[9 - i][-1] for i in range(10)).replace(".", "0").replace("#", "1"), 2)
    ]

inp = "".join(line for line in open("day20_input.txt").readlines()).split("\n\n")
tiles = dict()
for tile in inp:
    id, capture = tile.split(":\n")
    tiles[int(id.split()[1])] = createBorders(capture.split("\n"))

shares = {id: 0 for id in tiles}
for id1 in tiles:
    for id2 in tiles:
        if id1 == id2:
            continue
        for b1 in tiles[id1]:
            for b2 in tiles[id2]:
                if b1 == b2:
                    shares[id1] += 1
                    shares[id2] += 1

m = min(shares.values())
res = 1
for id, count in shares.items():
    if count == m:
        res *= id
print(res)
