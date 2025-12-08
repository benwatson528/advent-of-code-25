import os
from pathlib import Path

from main.day08.playground import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt"), 10) == 40


def test_p1_real():
    assert solve_p1(read_input("data/input.txt"), 1000) == 352584


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 25272


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 9617397716


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [tuple(int(x) for x in l.split(",")) for l in f.read().splitlines()]
