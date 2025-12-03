import os
from pathlib import Path

from main.day03.lobby import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 357


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 17408


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 3121910778619


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 172740584266849


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
