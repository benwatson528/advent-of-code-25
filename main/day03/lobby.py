def solve_p1(banks) -> int:
    return sum(
        int(int(sorted(b[:-1], reverse=True)[0] + max(b[b.index(sorted(b[:-1], reverse=True)[0]) + 1:]))) for b in
        banks)


def solve_p2(banks) -> int:
    def find_biggest_rec(b, n, j):
        return find_biggest_rec(b[b.index(max(b[:len(b) - n + 1])) + 1:], n - 1,
                                j + max(b[:len(b) - n + 1])) if n > 0 else j

    return sum(int(find_biggest_rec(b, 12, "")) for b in banks)
