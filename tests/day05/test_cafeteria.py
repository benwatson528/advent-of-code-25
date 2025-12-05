import os
from pathlib import Path

from main.day05.cafeteria import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 3


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 896


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
                ranges.append(range(int(l.split("-")[0]), int(l.split("-")[1]) + 1))
            else:
                available.append(int(l))
    return ranges, available
