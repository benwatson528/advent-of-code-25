ADJACENT = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (-1, -1), (1, 1)]


def find_num_adjacent(r, rolls) -> int: return sum((r[0] + d[0], r[1] + d[1]) in rolls for d in ADJACENT)


def solve_p1(rolls) -> int:
    return sum(find_num_adjacent(r, rolls) < 4 for r in rolls)


def solve_p2(rolls) -> int:
    total_removed = 0
    while to_remove := {r for r in rolls if find_num_adjacent(r, rolls) < 4}:
        total_removed += len(to_remove)
        rolls -= to_remove
    return total_removed
