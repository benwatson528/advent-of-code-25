def solve(splitters, start) -> int:
    num_splitter_hits = 0
    beam_tips = [start]
    # we know we go down 1 each turn even if it hits a splitter
    for _ in range(max(y for _, y in splitters)):
        new_beam_tips = set()
        for beam in beam_tips:
            # either move active splitters down or split them
            if (beam[0], beam[1] + 1) in splitters:
                num_splitter_hits += 1
                new_beam_tips.add((beam[0] - 1, beam[1] + 1))
                new_beam_tips.add((beam[0] + 1, beam[1] + 1))
            else:
                new_beam_tips.add((beam[0], beam[1] + 1))
        beam_tips = new_beam_tips
    return num_splitter_hits
