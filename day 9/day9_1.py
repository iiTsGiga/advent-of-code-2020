numbers = [int(num) for num in open("day9_input.txt")]

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
        print(numbers[i])
        break
    i += 1