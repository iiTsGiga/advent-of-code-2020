groups = [line.split() for line in "".join(line for line in open("day6_input.txt")).split("\n\n")]

count = 0
for group in groups:
    votes = group[0]
    for member in group[1:]:
        newVotes = ""
        for c in votes:
            if c in member:
                newVotes += c
        votes = newVotes
        if votes == "":
            break
    count += len(votes)

print(count)
