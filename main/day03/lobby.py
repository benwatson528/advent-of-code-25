def solve(banks, num_active_batteries) -> int:
    def find_biggest_rec(b, n, j):
        return find_biggest_rec(b[b.index(max(b[:len(b) - n + 1])) + 1:], n - 1,
                                j + max(b[:len(b) - n + 1])) if n > 0 else j

    return sum(int(find_biggest_rec(b, num_active_batteries, "")) for b in banks)
