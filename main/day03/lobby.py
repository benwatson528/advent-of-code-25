def solve(banks) -> int:
    joltage = 0
    for b in banks:
        biggest = sorted(b, reverse=True)[0]
        if b.index(biggest) == len(b) - 1:
            biggest = sorted(b, reverse=True)[1]
        right_max = max(b[b.index(biggest) + 1:])
        joltage += int(biggest + right_max)
    return joltage
