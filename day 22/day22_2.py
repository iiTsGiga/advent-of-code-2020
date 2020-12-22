def determineWinner(p1, p2, startSubGame=True):
    if len(p1) - 1 >= p1[0] and len(p2) - 1 >= p2[0]:
        return determineWinner(p1[1:p1[0] + 1], p2[1:p2[0] + 1])
    if not startSubGame:
        return p1[0] > p2[0]
    states = [(p1[:], p2[:])]
    while len(p1) and len(p2):
        if determineWinner(p1, p2, False):
            p1.append(p1.pop(0))
            p1.append(p2.pop(0))
        else:
            p2.append(p2.pop(0))
            p2.append(p1.pop(0))
        newState = (p1[:], p2[:])
        if newState in states:
            return True
        states.append(newState)
    return len(p1)

p1, p2 = open("day22_input.txt").read().split("\n\n")
p1 = [int(i) for i in p1.split("\n")[1:]]
p2 = [int(i) for i in p2.split("\n")[1:]]
determineWinner(p1, p2)
winner = p1 if len(p1) else p2
print(sum(winner[-i]*i for i in range(1, len(winner)+1)))
