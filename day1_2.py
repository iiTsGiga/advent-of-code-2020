nums = [int(line) for line in open("day1_1_input.txt").readlines()]

for i, n1 in enumerate(nums):
    for j, n2 in enumerate(nums[i+1:]):
        if n1 + n2 > 2020: continue
        for n3 in nums[j+1:]:
            if n1 + n2 + n3 == 2020:
                print(n1*n2*n3)
