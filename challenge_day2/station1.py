def solution_station_1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

test_numbers = {
    90: 2880067194370816000,
    2: 1,
    32: 2178309,
    50: 12586269025,
    86: 420196140727489660,
    44: 701408733,
    94: 19740274219868220000,
    80: 23416728348467684,
    62: 4052739537881
}


print(solution_station_1('87'))