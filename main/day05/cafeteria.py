def solve(ranges, available) -> int:
    return sum(any(x in r for r in ranges) for x in available)
