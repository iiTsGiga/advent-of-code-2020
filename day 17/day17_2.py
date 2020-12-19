def deepCopyCubes(cubes):
    return [[[[cube for cube in row] for row in layer] for layer in fourthDim] for fourthDim in cubes]

def expandSource(cubes):
    depth = len(cubes) + 2
    length = len(cubes[0]) + 2
    height = len(cubes[0][0]) + 2
    width = len(cubes[0][0][0]) + 2
    new_cubes = deepCopyCubes(cubes)
    new_cubes = [[[[False for _ in range(width)] for _ in range(height)] for _ in range(length)]] + new_cubes + [[[[False for _ in range(width)] for _ in range(height)] for _ in range(length)]]
    for w, fourthDim in enumerate(new_cubes):
        if w == 0 or w == depth - 1:
            continue
        new_cubes[w] = [[[False for _ in range(width)] for _ in range(height)]] + new_cubes[w] + [[[False for _ in range(width)] for _ in range(height)]]
        for z, layer in enumerate(new_cubes[w]):
            if z == 0 or z == length - 1:
                continue
            new_cubes[w][z] = [[False for _ in range(width)]] + new_cubes[w][z] + [[False for _ in range(width)]]
            for y, row in enumerate(new_cubes[w][z]):
                if y == 0 or y == height - 1:
                    continue
                new_cubes[w][z][y] = [False] + new_cubes[w][z][y] + [False]
    return new_cubes

def printCubes(cubes):
    for w, fourthDim in enumerate(cubes):
        for z, layer in enumerate(fourthDim):
            print(f"\nz={z-len(cubes[0])//2}, w={w-len(cubes)//2}")
            for y, row in enumerate(layer):
                for x, cube in enumerate(row):
                    print("#" if cube else ".", end="  ")
                print()
    print("\n\n----------------------------------------------------------------\n\n")

def countActiveNeighbors(cubes, xoff, yoff, zoff, woff):
    depth = len(cubes)
    length = len(cubes[0])
    height = len(cubes[0][0])
    width = len(cubes[0][0][0])
    neighbours = 0
    for w in range(woff - 1, woff + 2):
        if w < 0 or w >= depth:
            continue
        for z in range(zoff - 1, zoff + 2):
            if z < 0 or z >= length:
                continue
            for y in range(yoff - 1, yoff + 2):
                if y < 0 or y >= height:
                    continue
                for x in range(xoff - 1, xoff + 2):
                    if x < 0 or x >= width or (x == xoff and y == yoff and z == zoff and w == woff):
                        continue
                    neighbours += cubes[w][z][y][x]
    return neighbours

def simulate(cubes, cycles):
    if cycles == 0:
        res = 0
        for fourthDim in cubes:
            for layer in fourthDim:
                for row in layer:
                    res += row.count(True)
        return res
    new_cubes = expandSource(cubes)
    depth = len(cubes)
    length = len(cubes[0])
    height = len(cubes[0][0])
    width = len(cubes[0][0][0])
    for w, fourthDim in enumerate(new_cubes):
        for z, layer in enumerate(fourthDim):
            for y, row in enumerate(layer):
                for x, _ in enumerate(row):
                    activeNeighbors = countActiveNeighbors(cubes, x - 1, y - 1, z - 1, w - 1)
                    if x == 0 or x == width + 1 or y == 0 or y == height + 1 or z == 0 or z == length + 1 or w == 0 or w == depth + 1:
                        new_cubes[w][z][y][x] = activeNeighbors == 3
                    else:
                        new_cubes[w][z][y][x] = (cubes[w - 1][z - 1][y - 1][x - 1] and activeNeighbors == 2) or activeNeighbors == 3
    return simulate(new_cubes, cycles-1)

if __name__ == "__main__":
    inp = [line.strip() for line in open("day17_input.txt")]
    cubes = [[[[x == "#" for x in row] for row in inp]]]
    print(simulate(cubes, 6))
