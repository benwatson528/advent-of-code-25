from collections import deque


def solve(devices) -> int:
    return find_outs(devices, "you")


def find_outs(devices, start):
    num_paths = 0
    q = deque()
    q.append((start, set()))
    while q:
        n, visited = q.popleft()
        if n == "out":
            num_paths += 1
            continue
        for out in devices[n]:
            q.append((out, visited | {n}))
    return num_paths
