lines = [l.strip() for l in open("day13_input.txt").readlines()]
buses = [(n, int(x)) for n, x in enumerate(lines[1].split(",")) if x != "x"]
lcm = buses[0][1]
timestamp = -buses[0][0]

for delay, bus in buses[1:]:
    k = ((-delay % bus) - timestamp) * pow(lcm, -1, bus) % bus
    lcm_new = abs(lcm * bus)
    timestamp = (lcm * k + timestamp) % lcm_new
    lcm = lcm_new

print(timestamp)