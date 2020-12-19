nums = [int(line) for line in open("day1_1_input.txt").readlines()]

for i, n1 in enumerate(nums):
    for n2 in nums[i+1:]:
        if n1 + n2 == 2020:
            print(n1*n2)