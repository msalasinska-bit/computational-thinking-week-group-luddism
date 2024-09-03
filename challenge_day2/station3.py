def solution_station_3(num):
    return num % 3 == 0

test_numbers = [99, 52, 72, 42, 43, 21, 53, 72, 31, 64, 51]
results = {num: solution_station_3(num) for num in test_numbers}
print(results)

print(solution_station_3())
