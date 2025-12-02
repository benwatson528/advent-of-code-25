import os
from pathlib import Path

from main.day02.gift_shop import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 1227775554


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 19574776074


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for l in f.read().split(","):
            yield tuple(int(x) for x in l.split("-"))

