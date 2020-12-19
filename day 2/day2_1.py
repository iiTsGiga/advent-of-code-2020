database = [line.strip().split() for line in open("day2_1_input.txt").readlines()]

valid = 0
for rng, char, pw in database:
    lowest, highest = map(int, rng.split('-'))
    char = char[0]
    count = 0
    for c in pw:
        if c == char:
            if count == highest:
                break
            count += 1
    else:
        if count >= lowest:
            valid += 1

print(valid)
