def solve(ranges) -> int:
    invalid_ids = []
    for s in [str(i) for r in ranges for i in range(r[0], r[1] + 1)]:
        if s[:len(s) // 2] == s[len(s) // 2:]:
            invalid_ids.append(s)
    return sum(int(x) for x in invalid_ids)
