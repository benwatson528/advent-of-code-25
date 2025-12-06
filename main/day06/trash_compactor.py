def solve(ls) -> int:
    return sum(eval(l[-1].join(l[:-1])) for l in ls)
