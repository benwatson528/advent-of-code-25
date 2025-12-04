import os
from pathlib import Path

from main.day04.printing_department import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 13


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 1370


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 43


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 8437


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rolls = set()
        lines = f.read().splitlines()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "@":
                    rolls.add((x, y))
    return rolls
