def move(cups: list, i: int):
    indexValue = cups[i]
    destValue = cups[i] - 1
    pickup = []
    for _ in range(3):
        if i + 1 >= len(cups):
            pickup.append(cups.pop(0))
        else:
            pickup.append(cups.pop(i+1))
    while destValue not in cups:
        destValue -= 1
        if destValue <= 0:
            destValue = max(cups)
            break
    destIndex = cups.index(destValue)+1
    cups[:] = cups[:destIndex] + pickup + cups[destIndex:]
    return cups.index(indexValue)

cups = [int(x) for x in open("day23_input.txt").read()]
i = 0
for _ in range(100):
    i = (move(cups, i) + 1) % len(cups)
oneIndex = cups.index(1)
print("".join(str(x) for x in cups[oneIndex+1:] + cups[:oneIndex]))