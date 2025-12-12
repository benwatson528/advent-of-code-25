def solve(regions) -> int:
    return sum(sum(r[1]) * 9 <= r[0][0] * r[0][1] for r in regions)
