def search_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

print("Os números pares são", search_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)

print(count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)


