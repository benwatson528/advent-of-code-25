import itertools


def solve(red_tiles) -> int:
    return sorted(
        [((p1, p2), (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)) for p1, p2 in
         itertools.combinations(red_tiles, 2)],
        key=lambda x: -x[1])[0][1]
