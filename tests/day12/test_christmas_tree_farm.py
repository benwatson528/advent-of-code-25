import os
from pathlib import Path

from main.day12.christmas_tree_farm import solve


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 528


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        for l in f.read().splitlines():
            if "x" in l:
                yield (tuple(int(x) for x in l.split(":")[0].split("x")),
                       tuple(int(x) for x in l.split(": ")[1].split()))
