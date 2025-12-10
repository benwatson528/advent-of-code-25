import os
from pathlib import Path

from main.day10.factory import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input("data/test_input.txt")) == 7


def test_p1_real():
    assert solve_p1(read_input("data/input.txt")) == 512


def test_p2_simple():
    assert solve_p2(read_input("data/test_input.txt")) == 33


def test_p2_real():
    assert solve_p2(read_input("data/input.txt")) == 20415
    # 20463 too high
    # 20461 too high
    # 20415 too high



def read_input(file_name):
    manual = []
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for l in f.read().splitlines():
            indicators = list(l.split("]")[0][1:])
            buttons = [x.split(",") for x in l.split("] ")[1].split(" {")[0].replace("(", "").replace(")", "").split()]
            joltages = l.split("{")[1][:-1]
            manual.append((indicators, buttons, joltages))
    return manual