m = [line.strip() for line in open("day3_input.txt").readlines()]

steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
treeCount = 0

for step in steps:
    x, y = step
    trees = 0

    while y < len(m):
        trees += m[y][x] == '#'
        x += step[0]
        if x >= len(m[y]):
            x = x % len(m[y])
        y += step[1]

    if treeCount == 0:
        treeCount = trees
    else:
        treeCount *= trees

print(treeCount)
