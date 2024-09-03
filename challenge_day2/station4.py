def solution_station_4(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while (i * i) <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

test_numbers = [10, 87, 85, 22, 81, 46, 30, 79, 22, 2, 19, 32, 86, 96, 27, 64, 98, 53]
results = {num: solution_station_4(num) for num in test_numbers}
print(results)

print(solution_station_4())
