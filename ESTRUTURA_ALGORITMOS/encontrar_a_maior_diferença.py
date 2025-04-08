def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x - y))
    return result

# Usando sorted para ordenar a lista   

def maxxDiff(numbers):
    numbers = sorted(numbers)
    return numbers[-1] - numbers[0]

print("A maior diferença é", maxxDiff([1, 2, 5, 4, 3, 6, 7, 8, 9]))

# usando max e min

def MaxDiff(numbers):
    return max(numbers) - min(numbers)