# read data and replace empty with occupied (see first round from puzzles example)
seats = [[c for c in line.strip()] for line in open("day11_input.txt")]
w, h = len(seats[0]), len(seats)

def occupied_neighbors(seats, x, y, w, h):
    occupied = 0

    # look for above
    yoff = y - 1
    while yoff >= 0:
        occupied += seats[yoff][x] == "#"
        if seats[yoff][x] in "L#":
            break
        yoff -= 1

    # look for below
    yoff = y + 1
    while yoff < h:
        occupied += seats[yoff][x] == "#"
        if seats[yoff][x] in "L#":
            break
        yoff += 1

    # look for left
    xoff = x - 1
    while xoff >= 0:
        occupied += seats[y][xoff] == "#"
        if seats[y][xoff] in "L#":
            break
        xoff -= 1

    # look for right
    xoff = x + 1
    while xoff < w:
        occupied += seats[y][xoff] == "#"
        if seats[y][xoff] in "L#":
            break
        xoff += 1

    # look for diagonal TL
    xoff = x - 1
    yoff = y - 1
    while xoff >= 0 and yoff >= 0:
        occupied += seats[yoff][xoff] == "#"
        if seats[yoff][xoff] in "L#":
            break
        xoff -= 1
        yoff -= 1

    # look for diagonal TR
    xoff = x + 1
    yoff = y - 1
    while xoff < w and yoff >= 0:
        occupied += seats[yoff][xoff] == "#"
        if seats[yoff][xoff] in "L#":
            break
        xoff += 1
        yoff -= 1

    # look for diagonal BL
    xoff = x - 1
    yoff = y + 1
    while xoff >= 0 and yoff < h:
        occupied += seats[yoff][xoff] == "#"
        if seats[yoff][xoff] in "L#":
            break
        xoff -= 1
        yoff += 1

    # look for diagonal BR
    xoff = x + 1
    yoff = y + 1
    while xoff < w and yoff < h:
        occupied += seats[yoff][xoff] == "#"
        if seats[yoff][xoff] in "L#":
            break
        xoff += 1
        yoff += 1

    return occupied

while True:
    old_seats = [[seat for seat in row] for row in seats]
    for y, row in enumerate(old_seats):
        for x, seat in enumerate(row):
            if seat == ".":
                continue
            neighbors = occupied_neighbors(old_seats, x, y, w, h)
            if seat == "L" and neighbors == 0:
                seats[y][x] = "#"
            elif seat == "#" and neighbors >= 5:
                seats[y][x] = "L"
    if seats == old_seats:
        break

occupied = 0
for row in seats:
    occupied += row.count("#")
print(occupied)