inp = "".join(open("day16_input.txt").readlines()).split("\n\n")
rules = [line.split(": ")[1].split(" or ") for line in inp[0].split("\n")]

# get every valid number
available = set()
for rule in rules:
    f, t = map(int, rule[0].split("-"))
    for i in range(f, t + 1):
        available.add(i)
    f, t = map(int, rule[1].split("-"))
    for i in range(f, t + 1):
        available.add(i)

# filter invalid numbers
tickets = [map(int, line.split(",")) for line in inp[2].split("\n")[1:]]
invalid = []
for ticket in tickets:
    for num in ticket:
        if num not in available:
            invalid.append(num)

print(sum(invalid))