numbers = [int(num) for num in open("day9_input.txt")]

invalid = 0

i = 25
while i < len(numbers):
    j = i - 25
    found = False
    while j < i and not found:
        k = j + 1
        while k < i:
            if numbers[j] + numbers[k] == numbers[i]:
                found = True
                break
            k += 1
        j += 1
    if not found:
        invalid = numbers[i]
        break
    i += 1

i = 0
while i < len(numbers) - 1:
    j = i + 1
    while j < len(numbers):
        if sum(numbers[i:j]) == invalid:
            print(min(numbers[i:j]) + max(numbers[i:j]))
            exit()
        j += 1
    i += 1
