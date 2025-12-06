import os
from pathlib import Path

from main.day06.trash_compactor import solve_p1, solve_p2


def test_p1_simple():
    assert solve_p1(read_input_p1("data/test_input.txt")) == 4277556


def test_p1_real():
    assert solve_p1(read_input_p1("data/input.txt")) == 6343365546996


def test_p2_simple():
    assert solve_p2(read_input_p2("data/test_input.txt")) == 3263827


def test_p2_real():
    assert solve_p2(read_input_p2("data/input.txt")) == 11136895955912


def read_input_p1(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        rows = []
        lines = f.read().splitlines()
        for j, a in enumerate(lines):
            for i, b in enumerate(lines[j].split()):
                if len(rows) <= i:
                    rows.append([])
                rows[i].append(b)
        return rows


def read_input_p2(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        cols = []
        lines = f.read().splitlines()
        for j, a in enumerate(lines):
            cols.append([])
            for i, b in enumerate(reversed(lines[j])):
                cols[j].append(b)
        return cols
