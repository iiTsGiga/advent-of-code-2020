code = [line.strip().split() for line in open("day8_input.txt")]
code = [(instruction, int(value)) for instruction, value in code]

def execute(code):
    executed = [False for _ in iter(code)]
    accumulator = i = 0
    while i < len(code):
        if executed[i]:
            return False, accumulator
        executed[i] = True
        instruction, value = code[i]
        accumulator += (instruction == "acc") * value
        i += (instruction == "jmp") * value + (instruction != "jmp")
    return True, accumulator

# part 1 - 1451
print(execute(code)[1])

# part 2 - 1160
for i, line in enumerate(code):
    instruction, value = line
    if instruction == "acc":
        continue
    instruction = (instruction == "jmp") * "nop" + (instruction == "nop") * "jmp"
    terminated, accumulator = execute(code[:i] + [(instruction, value)] + code[i+1:])
    if terminated:
        print(accumulator)
        exit()