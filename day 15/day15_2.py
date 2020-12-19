inp = [int(n) for n in open("day15_input.txt").readline().strip().split(",")]

def spoken_at(nums, at):
    spoken = {n: i for i, n in enumerate(nums[:-1])}
    for i in range(len(nums) - 1, at - 1):
        nums.append(i - spoken.get(nums[i], i))
        spoken[nums[i]] = i
    return nums[-1]

print(spoken_at(inp, 30000000))