def solve_p1(ls) -> int:
    return sum(eval(l[-1].join(l[:-1])) for l in ls)


def solve_p2(ls) -> int:
    answers = []
    equation = []
    operator = None
    for col in range(len(ls[0])):
        row = ""
        for j in range(len(ls)):
            c = ls[j][col]
            if c in ("+", "*"):
                operator = c
            else:
                row += c
        if not row.strip():
            answers.append(eval(operator.join(equation)))
            equation = []
            operator = None
        if row.strip():
            equation.append(row.strip())
        print()
    answers.append(eval(operator.join(equation)))
    return sum(answers)
