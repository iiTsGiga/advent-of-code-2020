p1, p2 = open("day22_input.txt").read().split("\n\n")
p1 = [int(i) for i in p1.split("\n")[1:]]
p2 = [int(i) for i in p2.split("\n")[1:]]
while len(p1) and len(p2):
    if p1[0] > p2[0]:
        p1.append(p1.pop(0))
        p1.append(p2.pop(0))
    else:
        p2.append(p2.pop(0))
        p2.append(p1.pop(0))
winner = p1 if len(p1) else p2
print(sum(winner[-i]*i for i in range(1, len(winner)+1)))
