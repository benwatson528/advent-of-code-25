import os
from pathlib import Path

from main.day03.lobby import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 2) == 357


def test_p1_real():
    assert solve(read_input("data/input.txt"), 2) == 17408


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), 12) == 3121910778619


def test_p2_real():
    assert solve(read_input("data/input.txt"), 12) == 172740584266849


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()
