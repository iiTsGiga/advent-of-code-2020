print(sum([len(set(line.replace("\n", ""))) for line in "".join(open("day6_input.txt")).split("\n\n")]))
