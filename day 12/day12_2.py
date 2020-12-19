directions = [(line[0], int(line.strip()[1:])) for line in open("day12_input.txt")]

data = [0, 0, 10, -1, 0]

for d in directions:
    data[2] += ((d[0] == "E") - (d[0] == "W")) * d[1]
    data[3] += ((d[0] == "S") - (d[0] == "N")) * d[1]
    data[0] += data[2] * d[1] * (d[0] == "F")
    data[1] += data[3] * d[1] * (d[0] == "F")
    for i in range((d[0] in "LR")*d[1]//90):
        data[4] = data[2]
        data[2] = data[3] * (1 - (d[0] == "R") * 2) * (d[0] in "LR") + data[2] * (d[0] not in "LR")
        data[3] = data[4] * (1 - (d[0] == "L") * 2) * (d[0] in "LR") + data[3] * (d[0] not in "LR")

print(abs(data[0]) + abs(data[1]))
