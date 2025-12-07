from functools import lru_cache


def solve_p1(splitters, start) -> int:
    num_splitter_hits = 0
    beam_tips = [start]
    for _ in range(max(y for _, y in splitters)):
        new_beam_tips = set()
        for beam in beam_tips:
            if (beam[0], beam[1] + 1) in splitters:
                num_splitter_hits += 1
                new_beam_tips.add((beam[0] - 1, beam[1] + 1))
                new_beam_tips.add((beam[0] + 1, beam[1] + 1))
            else:
                new_beam_tips.add((beam[0], beam[1] + 1))
        beam_tips = new_beam_tips
    return num_splitter_hits


def solve_p2(splitters, start) -> int:
    return move(start, frozenset(splitters), max(y for _, y in splitters)) + 1


@lru_cache
def move(beam, splitters, max_depth) -> int:
    if beam[1] == max_depth:
        return 0
    elif (beam[0], beam[1] + 1) in splitters:
        return move((beam[0] - 1, beam[1] + 1), splitters, max_depth) + move(
            (beam[0] + 1, beam[1] + 1), splitters, max_depth) + 1
    else:
        return move((beam[0], beam[1] + 1), splitters, max_depth)
