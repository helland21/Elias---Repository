def even_numbers_10_to_20(numbers: list) -> list:
    return [num for num in numbers if 10 <= num <= 20 and num % 2 == 0]

#Eksempel
numbers = [1, 7, 14, 16, 22]
result = even_numbers_10_to_20(numbers)
print(result) # Output: 14 og 16 