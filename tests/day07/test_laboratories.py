import os
from pathlib import Path

from main.day07.laboratories import solve


def test_p1_simple():
    assert solve(*read_input("data/test_input.txt")) == 21


def test_p1_real():
    assert solve(*read_input("data/input.txt")) == 1602


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        splitters = set()
        start = None
        lines = f.read().splitlines()
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "^":
                    splitters.add((x, y))
                elif lines[y][x] == "S":
                    start = x, y
    return splitters, start
