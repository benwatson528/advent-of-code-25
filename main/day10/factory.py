from collections import deque, defaultdict
from string import ascii_lowercase

from z3 import Int, Optimize


def solve_p1(manual) -> int:
    return sum(toggle_p1(m[0], m[1]) for m in manual)


def solve_p2(manual) -> int:
    num_turns = 0
    for m in manual:
        components = defaultdict(list)
        joltages = [int(x) for x in m[2].split(",")]
        letters = set()
        for j in range(len(joltages)):
            components[j] = []
        for i, buttons in enumerate(m[1]):
            for b in buttons:
                components[int(b)].append(ascii_lowercase[i])
                letters.add(ascii_lowercase[i])
        num_turns += solve_equations(components, joltages, letters)
    return num_turns


def solve_equations(components, joltages, letters):
    a = Int('a')
    b = Int('b')
    c = Int('c')
    d = Int('d')
    e = Int('e')
    f = Int('f')
    g = Int('g')
    h = Int('h')
    i = Int('i')
    j = Int('j')
    k = Int('k')
    l = Int('l')
    m = Int('m')
    n = Int('n')
    o = Int('o')
    p = Int('p')
    q = Int('q')
    r = Int('r')
    s = Int('s')
    t = Int('t')
    u = Int('u')
    v = Int('v')
    w = Int('w')
    x = Int('x')
    y = Int('y')
    z = Int('z')

    all_vars = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

    solver = Optimize()
    for ascii_char in ascii_lowercase[:len(letters)]:
        char_ = f"{ascii_char} >= 0"
        solver.add(eval(char_))
    for comp, ls in components.items():
        solver.add(eval(f"{" + ".join(ls)} == {joltages[comp]}"))

    solver.minimize(sum(all_vars[:len(letters)]))
    solver.check()
    model = solver.model()
    return sum(int(model[model_result].as_string()) for model_result in solver.model())


def toggle_p1(expected_indicator, buttons):
    q = deque()
    seen = set()
    q.append((["."] * len(expected_indicator), 0))
    while q:
        q = deque(sorted(q, key=lambda x: x[1]))
        indicator, num_presses = q.popleft()
        for button in buttons:
            copied_indicator = indicator.copy()
            for b in button:
                copied_indicator[int(b)] = "." if copied_indicator[int(b)] == "#" else "#"
            if copied_indicator == expected_indicator:
                return num_presses + 1
            if "".join(copied_indicator) not in seen:
                q.append((copied_indicator, num_presses + 1))
            seen.add("".join(copied_indicator))
    return -1
