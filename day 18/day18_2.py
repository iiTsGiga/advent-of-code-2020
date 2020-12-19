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
		ind = 1
		if "+" in parts:
			for i, part in enumerate(parts):
				if part == "+":
					ind = i
					break
		parts = parts[:ind-1] + [str(eval(parts[ind-1]+parts[ind]+parts[ind+1]))] + parts[ind+2:]
	return parts[0]

res = 0
for task in tasks:
	res += int(solveTask(task))
print(res)