# read data and replace empty with occupied (see first round from puzzles example)
seats = [[(c == ".") * "." + (c == "L") * "#" for c in line.strip()] for line in open("day11_input.txt")]

# count the adjacent
def occupied_neighbors(seats, x, y):
    occupied = 0
    for yoff in range(y-1, y+2):
        if yoff < 0 or yoff >= len(seats):
            continue
        for xoff in range(x-1, x+2):
            if (xoff == x and yoff == y) or xoff < 0 or xoff >= len(seats[y]):
                continue
            if seats[yoff][xoff] == "#":
                occupied += 1
    return occupied

while True:
    old_seats = [[seat for seat in row] for row in seats]
    for y, row in enumerate(old_seats):
        for x, seat in enumerate(row):
            if seat == ".":
                continue
            neighbors = occupied_neighbors(old_seats, x, y)
            if seat == "L" and neighbors == 0:
                seats[y][x] = "#"
            elif seat == "#" and neighbors >= 4:
                seats[y][x] = "L"
    if seats == old_seats:
        break

occupied = 0
for row in seats:
    occupied += row.count("#")
print(occupied)