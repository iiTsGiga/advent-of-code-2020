def deepCopyCubes(cubes):
    return [[[cube for cube in row] for row in layer] for layer in cubes]

def expandSource(cubes):
    d = len(cubes) + 2
    h = len(cubes[0]) + 2
    w = len(cubes[0][0]) + 2
    new_cubes = deepCopyCubes(cubes)
    new_cubes = [[[False for _ in range(w)] for _ in range(h)]] + new_cubes + [[[False for _ in range(w)] for _ in range(h)]]  # create extra 2 layers in the front and back
    for z, layer in enumerate(new_cubes):
        if z == 0 or z == d - 1:  # dont change the newly created 2 layers
            continue
        new_cubes[z] = [[False for _ in range(w)]] + new_cubes[z] + [[False for _ in range(w)]]  # create extra 2 rows per layer at the top and bottom
        for y, row in enumerate(new_cubes[z]):
            if y == 0 or y == h - 1:  # dont change the newly created 2 rows
                continue
            new_cubes[z][y] = [False] + new_cubes[z][y] + [False]  # create extra 2 columns per row at the left and right
    return new_cubes

def printCubes(cubes):
    N = len(cubes)
    for z, layer in enumerate(cubes):
        print(f"\nz={z-N//2}")
        for y, row in enumerate(layer):
            for x, cube in enumerate(row):
                print("#" if cube else ".", end="  ")
            print()
    print("\n\n----------------------------------------------------------------\n\n")

def countActiveNeighbors(cubes, xoff, yoff, zoff):
    d = len(cubes)
    h = len(cubes[0])
    w = len(cubes[0][0])
    neighbours = 0
    for z in range(zoff - 1, zoff + 2):
        if z < 0 or z >= d:
            continue
        for y in range(yoff - 1, yoff + 2):
            if y < 0 or y >= h:
                continue
            for x in range(xoff - 1, xoff + 2):
                if 0 <= x < w and (x != xoff or y != yoff or z != zoff):
                    neighbours += cubes[z][y][x]
    return neighbours

def simulate(cubes, cycles):
    if cycles == 0:
        res = 0
        for layer in cubes:
            for row in layer:
                res += row.count(True)
        return res
    new_cubes = expandSource(cubes)
    d = len(cubes)
    h = len(cubes[0])
    w = len(cubes[0][0])
    for z, layer in enumerate(new_cubes):
        for y, row in enumerate(layer):
            for x, _ in enumerate(row):
                activeNeighbors = countActiveNeighbors(cubes, x - 1, y - 1, z - 1)
                if x == 0 or x == w + 1 or y == 0 or y == h + 1 or z == 0 or z == d + 1:
                    new_cubes[z][y][x] = activeNeighbors == 3
                else:
                    new_cubes[z][y][x] = (cubes[z - 1][y - 1][x - 1] and activeNeighbors == 2) or activeNeighbors == 3
    return simulate(new_cubes, cycles-1)

if __name__ == "__main__":
    inp = [line.strip() for line in open("day17_input.txt")]
    cubes = [[[x == "#" for x in row] for row in inp]]
    print(simulate(cubes, 6))
