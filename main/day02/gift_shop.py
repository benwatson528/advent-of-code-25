import itertools


def solve_p1(ranges) -> int:
    invalid_ids = []
    for s in [str(i) for r in ranges for i in range(r[0], r[1] + 1)]:
        if s[:len(s) // 2] == s[len(s) // 2:]:
            invalid_ids.append(s)
    return sum(int(x) for x in invalid_ids)


def solve_p2(ranges) -> int:
    invalid_ids = []
    for s in [str(i) for r in ranges for i in range(r[0], r[1] + 1)]:
        for n in range(1, len(s) // 2 + 1):
            if len(s) % n == 0:
                if all(s[:n] == b for b in ["".join(x) for x in itertools.batched(s, n)]):
                    invalid_ids.append(s)
                    break
    return sum(int(x) for x in invalid_ids)
