data = [line.strip() for line in open("day13_input.txt")]
timestamp = int(data[0])
bus_ids = [int(n) for n in data[1].split(",") if n.isdigit()]

lowest = bus_ids[0]
lowest_ttw = time_to_wait = lowest - (timestamp % lowest)

for id in bus_ids:
    time_to_wait = id - (timestamp % id)
    if time_to_wait < lowest_ttw:
        lowest = id
        lowest_ttw = time_to_wait

print(lowest*lowest_ttw)