code = [line.strip() for line in open("day8_input.txt")]

#1451

executed = []
accumulator = 0
i = 0
while i not in executed:
    executed.append(i)
    instruction, value = code[i].split()
    if instruction == "acc":
        accumulator += int(value)
        i += 1
    elif instruction == "jmp":
        i += int(value)
    elif instruction == "nop":
        i += 1

print(accumulator)