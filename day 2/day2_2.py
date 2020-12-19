database = [line.split() for line in open("day2_1_input.txt").readlines()]

valid = 0
for rng, char, pw in database:
    i1, i2 = map(int, rng.split('-'))
    if (pw[i1-1] == char[0]) ^ (pw[i2-1] == char[0]):
        valid += 1

print(valid)
