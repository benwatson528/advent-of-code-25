import os

from pathlib import Path

from main.day06.trash_compactor import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == 4277556


def test_p1_real():
    assert solve(read_input("data/input.txt")) == 6343365546996


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rows = []
        lines = f.read().splitlines()
        for j, a in enumerate(lines):
            for i, b in enumerate(lines[j].split()):
                if len(rows) <= i:
                    rows.append([])
                rows[i].append(b)
        return rows
