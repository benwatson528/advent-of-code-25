def solve_p1(banks) -> int:
    joltage = 0
    for b in banks:
        biggest = sorted(b[:-1], reverse=True)[0]
        right_max = max(b[b.index(biggest) + 1:])
        joltage += int(biggest + right_max)
    return joltage


def find_biggest_rec(b, n, j):
    return find_biggest_rec(b, n - 1, j) if n > 0 else j


def solve_p2(banks) -> int:
    joltage = 0
    for b in banks:
        biggest = find_biggest_rec(b, 12, "")
        joltage += int(biggest)
    return joltage
