import os
from pathlib import Path

from main.day09.movie_theater import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 50


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 4733727792


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return [(int(l.split(",")[0]), int(l.split(",")[1])) for l in f.read().splitlines()]

