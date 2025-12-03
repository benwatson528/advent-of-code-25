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
        num_zeroes += v // 100
        cropped_v = v % 100
        magnitude = 1 if d == "R" else -1
        uncropped_end = current + (magnitude * cropped_v)
        if ((uncropped_end < 0 or uncropped_end > 99) and current != 0) or uncropped_end == 0:
            num_zeroes += 1
        current = uncropped_end % 100
    return num_zeroes
