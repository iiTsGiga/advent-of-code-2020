inp = "".join(open("day16_input.txt").readlines()).split("\n\n")
rules = [line for line in inp[0].split("\n")]
available = set()

# invalid tickets - get valid numbers
for rule in [rule.split(": ")[1].split(" or ") for rule in rules]:
    f, t = map(int, rule[0].split("-"))
    for i in range(f, t + 1):
        available.add(i)
    f, t = map(int, rule[1].split("-"))
    for i in range(f, t + 1):
        available.add(i)

# invalid tickets - filter valid tickets
tickets = [list(map(int, line.split(","))) for line in inp[2].split("\n")[1:]]
valid = []
for ticket in tickets:
    for num in ticket:
        if num not in available:
            break
    else:
        valid.append(ticket)

# get fields with their ranges
# field_name: [[f, t], [f, t], [possible_index1, ...]]
fields = dict()
for rule in rules:
    field, rng = rule.split(": ")
    rng_low, rng_high = [list(map(int, r.split("-"))) for r in rng.split(" or ")]
    fields[field] = [rng_low, rng_high, -1]

# look for possible indeces for every field
for field in fields:
    available = set()
    for i in range(fields[field][0][0], fields[field][0][1] + 1):
        available.add(i)
    for i in range(fields[field][1][0], fields[field][1][1] + 1):
        available.add(i)
    possible_indeces = [_ for _ in range(len(fields))]
    for ticket in valid:
        for i, num in enumerate(ticket):
            if num not in available:
                possible_indeces.remove(i)
                break
    fields[field][2] = possible_indeces

# filter possible indeces entrys in fields which only have one possible index
# until every field only has one possible index left
found_indeces = False
while not found_indeces:
    for field in fields:
        if type(fields[field][2]) == list and len(fields[field][2]) == 1:
            fields[field][2] = fields[field][2][0]
            for f in fields:
                if type(fields[f][2]) == list:
                    fields[f][2].remove(fields[field][2])
            break
    found_indeces = True
    for field in fields:
        if type(fields[field][2]) == list:
            found_indeces = False
            break

# multiply together the "departure" fields in my ticket
myticket = list(map(int, inp[1].split("\n")[1].split(",")))
result = 1
for f in fields:
    if f.startswith("departure"):
        result *= myticket[fields[f][2]]

print(result)
