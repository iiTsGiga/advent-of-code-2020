tasks = [line.strip() for line in open("day18_input.txt")]

def solveTask(task):
    while "(" in task:
        pOpen = 0
        pClose = 0
        for i, c in enumerate(task):
            if c == "(":
                pOpen = i
            elif c == ")":
                pClose = i
                break
        task = task[:pOpen] + solveTask(task[pOpen + 1:pClose]) + task[pClose+1:]
    parts = task.split()
    while len(parts) != 1:
        parts = [str(eval(parts[0]+parts[1]+parts[2]))] + parts[3:]
    return parts[0]

res = 0
for task in tasks:
    res += int(solveTask(task))
print(res)