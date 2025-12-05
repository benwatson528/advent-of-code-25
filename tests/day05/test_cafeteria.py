import os
from pathlib import Path

from main.day05.cafeteria import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(*read_input("data/test_input.txt")) == 3


def test_p1_real():
    assert solve_p1(*read_input("data/input.txt")) == 896


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")[0]) == 14


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")[0]) == 346240317247002


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        is_ranges = True
        ranges = []
        available = []
        for l in f.read().splitlines():
            if not l:
                is_ranges = False
                continue
            if is_ranges:
                ranges.append(range(int(l.split("-")[0]), int(l.split("-")[1])))
            else:
                available.append(int(l))
    return ranges, available
