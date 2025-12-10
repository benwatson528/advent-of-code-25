from collections import deque, defaultdict
from string import ascii_lowercase

from z3 import Int, Solver


def solve_p1(manual) -> int:
    return sum(toggle_p1(m[0], m[1]) for m in manual)


def solve_p2(manual) -> int:
    num_turns = 0
    for m in manual:
        buttons = m[1]
        components = defaultdict(list)
        joltages = [int(x) for x in m[2].split(",")]
        for j in range(len(joltages)):
            components[j] = []
        for i, buttons in enumerate(m[1]):
            for b in buttons:
                components[int(b)].append(ascii_lowercase[i])
        num_turns += solve_equations(components, joltages)
    return num_turns


def solve_equations(components, joltages):
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

    # equations = []
    solver = Solver()
    for ascii_char in ascii_lowercase[:26]:
        solver.add(eval(f"{ascii_char} >= 0"))
    for comp, ls in components.items():
        solver.add(eval(f"{" + ".join(ls)} == {joltages[comp]}"))
    check = solver.check()
    model = solver.model()
    ans = 0
    for model_result in model:
        ans += int(model[model_result].as_string())
    return ans  # return sum(int(model[model_result]) for model_result in model)


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
