import os
from pathlib import Path

from main.day04.printing_department import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 13


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 1370


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rolls = set()
        lines = f.read().splitlines()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "@":
                    rolls.add((x, y))
    return rolls
