directions = [(line[0], int(line.strip()[1:])) for line in open("day12_input.txt")]

data = [0, 0, 1]

for d in directions:
    data[0] += (d[0] == "F") * ((data[2] == 1) - (data[2] == 3)) * d[1] + ((d[0] == "E") - (d[0] == "W")) * d[1]
    data[1] += (d[0] == "F") * ((data[2] == 2) - (data[2] == 0)) * d[1] + ((d[0] == "S") - (d[0] == "N")) * d[1]
    data[2] = (data[2] + ((d[0] == "R") - (d[0] == "L")) * (d[1] // 90)) % 4

print(abs(data[0]) + abs(data[1]))
