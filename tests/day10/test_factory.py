import os
from pathlib import Path

from main.day10.factory import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 7


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 0


def read_input(file_name):
    manual = []
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for l in f.read().splitlines():
            indicator = l.split("]")[0][1:]
            button = [x.split(",") for x in l.split("] ")[1].split(" {")[0].replace("(", "").replace(")", "").split()]
            joltage = l.split("{")[1][:-1]
            manual.append((indicator, button, joltage))
    return manual