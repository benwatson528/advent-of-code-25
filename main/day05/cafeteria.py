def solve_p1(ranges, available) -> int:
    return sum(any(x in range(r.start, r.stop + 1) for r in ranges) for x in available)


def solve_p2(ranges) -> int:
    final_ranges = set()
    sorted_ranges = sorted(ranges, key=lambda x: x.start)
    low, high = sorted_ranges[0].start, sorted_ranges[0].stop
    for r in sorted_ranges[1:]:
        # overlap found, expand the end and keep going
        if r.start <= high < r.stop:
            high = r.stop
        # no overlap found, close the existing window and start a new one
        elif not (r.start <= high >= r.stop):
            final_ranges.add((low, high))
            low, high = r.start, r.stop
    if high > max(r[1] for r in final_ranges):
        final_ranges.add((low, high))
    return sum(r[1] + 1 - r[0] for r in final_ranges)
