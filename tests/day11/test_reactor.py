import os
from collections import defaultdict
from pathlib import Path

from main.day11.reactor import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 5


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 511


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        devices = defaultdict(list)
        for l in f.read().splitlines():
            devices[l.split(": ")[0]] = l.split(": ")[1].split()
    return devices
