import re


def read_puzzle(fname):
    with open(fname, mode="r", encoding="UTF-8") as f:
        return [line.strip() for line in f.readlines()]


def solve_pt_one(puzzle):
    output = 0
    for line in puzzle:
        mul_cmds = re.findall(
            r"mul\(\b\d{1,3}\b,\b\d{1,3}\b\)",
            line,
        )
        for mul in mul_cmds:
            product = mul[4:-1].split(",")
            product = list(map(int, product))
            product = product[0] * product[1]
            output += product

    return output


def solve_pt_two(puzzle):
    output = 0
    enabled = True
    for line in puzzle:
        mul_cmds = re.findall(
            r"mul\(\b\d{1,3}\b,\b\d{1,3}\b\)|do\(\)|don't\(\)", line
        )
        for mul in mul_cmds:
            if mul == "don't()":
                enabled = False
            elif mul == "do()":
                enabled = True
            if mul.startswith("mul") and enabled:
                mul = mul[4:-1].split(",")
                product = int(mul[0]) * int(mul[1])
                output += product

    return output


if __name__ == "__main__":
    fname = "input.txt"
    # fname = "example.txt"
    puzzle = read_puzzle(fname)
    solutionOne = solve_pt_one(puzzle)
    solutionTwo = solve_pt_two(puzzle)
    print(solutionOne, solutionTwo)
