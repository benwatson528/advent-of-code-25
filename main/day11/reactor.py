from collections import deque
from functools import cache


def solve_p1(devices) -> int:
    num_paths = 0
    q = deque()
    q.append(("you", set()))
    while q:
        n, visited = q.popleft()
        if n == "out":
            num_paths += 1
            continue
        for out in devices[n]:
            q.append((out, visited | {n}))
    return num_paths


def solve_p2(devices) -> int:
    global DEVICES
    DEVICES = devices
    return traverse_rec("svr", False, False)


@cache
def traverse_rec(current, seen_dac, seen_fft):
    if current == "out":
        return 1 if seen_dac and seen_fft else 0
    else:
        ans = 0
        for output in DEVICES[current]:
            new_dac = seen_dac or output == "dac"
            new_fft = seen_fft or output == "fft"
            ans += traverse_rec(output, new_dac, new_fft)
        return ans
