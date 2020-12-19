adapters = sorted([int(line.strip()) for line in open("day10_input.txt")] + [0])
adapters.append(adapters[-1]+3)

diffs = [0, 0]
for i, adapter in enumerate(adapters[:-1]):
    diffs[(adapters[i+1] - adapter)//2] += 1

print(diffs[0] * diffs[1])
