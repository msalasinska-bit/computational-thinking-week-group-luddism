import math 

def solution_station_6(num):
    return math.sin(num)

test_numbers = [0.9, 0.3, 0.4, 1.7]

results = {num: solution_station_6(num) for num in test_numbers}

print(results)
print(solution_station_6)



