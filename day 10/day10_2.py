adapters = sorted([int(line.strip()) for line in open("day10_input.txt")] + [0])
adapters.append(adapters[-1]+3)

diffs = [adapters[i+1]-adapter for i, adapter in enumerate(adapters[:-1])]

counter = 0
combinations = 1
for diff in diffs:
    if diff == 1:
        counter += 1
    else:
        if counter > 1:
            combinations *= sum(range(1, counter)) + 1
        counter = 0

print(combinations)