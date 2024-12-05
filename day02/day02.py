print("Day 02")

with open("input.txt") as f:
    input = f.read()


def unsafe_index(numbers):
    increasing = numbers[0] < numbers[1]
    for i in range(0, len(numbers) - 1):
        if (
            (numbers[i] < numbers[i + 1]) != increasing
            or numbers[i] == numbers[i + 1]
            or abs(numbers[i] - numbers[i + 1]) > 3
        ):
            return i
    return None


completely_safe_count = 0
skip_safe_count = 0
for line in input.split("\n"):
    numbers = list(map(int, line.split(" ")))

    index_to_remove = unsafe_index(numbers)
    if index_to_remove == None:
        completely_safe_count += 1
        skip_safe_count += 1
        continue

    for removed in [0, index_to_remove, index_to_remove + 1]:
        if removed >= len(numbers):
            continue
        numbers2 = numbers[:]
        numbers2.pop(removed)
        if unsafe_index(numbers2) == None:
            skip_safe_count += 1
            break
    
print("Completely safe: " + str(completely_safe_count))
print("Somewhat safe: " + str(skip_safe_count))
