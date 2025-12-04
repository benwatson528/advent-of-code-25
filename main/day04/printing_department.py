ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (-1, -1), (1, 1)]


def solve(rolls) -> int:
    return sum(sum((r[0] + d[0], r[1] + d[1]) in rolls for d in ADJACENT) < 4 for r in rolls)
