import os
from collections import defaultdict
from pathlib import Path

from main.day11.reactor import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input_p1.txt")) == 5


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 511


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 458618114529380


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        devices = defaultdict(list)
        for l in f.read().splitlines():
            devices[l.split(": ")[0]] = l.split(": ")[1].split()
    return devices
