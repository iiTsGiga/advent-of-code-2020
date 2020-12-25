keys = list(map(int, open("day25_input.txt").read().split("\n")))
x = 0
while pow(7, x, 20201227) != keys[0]:
    x += 1
print(pow(keys[1], x, 20201227))
