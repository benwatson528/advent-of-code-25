import os
from pathlib import Path

from main.day01.secret_entrance import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 3


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 1123


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 8


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 6695


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for l in f.read().splitlines():
            yield l[0], int(l[1:])
