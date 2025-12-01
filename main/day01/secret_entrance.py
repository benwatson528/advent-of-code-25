import math


def solve_p1(movements, current=50) -> int:
    num_zeroes = 0
    for d, v in movements:
        magnitude = 1 if d == "R" else -1
        current = (current + (magnitude * v)) % 100
        num_zeroes += 1 if current == 0 else 0
    return num_zeroes


def solve_p2(movements, current=50) -> int:
    num_zeroes = 0
    for d, v in movements:
        num_zeroes += math.floor(v / 100)
        v = v % 100
        magnitude = 1 if d == "R" else -1
        net_movement = current + (magnitude * v)
        if current + net_movement > 99 or current + net_movement < 0:
            num_zeroes += 1
        current = net_movement % 100
    return num_zeroes


def solve_p2_slow(movements, current=50) -> int:
    num_zeroes = 0
    for d, v in movements:
        magnitude = 1 if d == "R" else -1
        for x in range(v):
            current += magnitude
            if current < 0:
                current = 99
            elif current > 99:
                current = 0
            if current == 0:
                num_zeroes += 1
    return num_zeroes
