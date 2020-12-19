m = [line.strip() for line in open("day3_input.txt").readlines()]

x = 3
y = 1
trees = 0

while y < len(m):
    if m[y][x] == '#':
        trees += 1
    x += 3
    if x >= len(m[y]):
        x = x % len(m[y])
    y += 1

print(trees)
