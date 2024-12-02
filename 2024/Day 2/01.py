def read_puzzle(fname):
    puzzle = []
    with open(fname, mode="r", encoding="UTF-8") as f:
        for line in f.readlines():
            line = line.strip().split()
            report = list(map(int, line))
            puzzle.append(report)
    return puzzle


def solve_pt_one(puzzle):
    def difference_in_bound(elem1, elem2):
        return abs(elem1 - elem2) >= 1 and abs(elem1 - elem2) <= 3

    safe_reports = 0
    for report in puzzle:
        safe = True
        increasing = report[0] < report[1]

        for i in range(len(report) - 1):
            in_bound = difference_in_bound(report[i], report[i + 1])

            if not in_bound:
                safe = False
                break
            if increasing and report[i] > report[i + 1]:
                safe = False
                break
            if not increasing and report[i] < report[i + 1]:
                safe = False
                break

        if safe:
            safe_reports += 1

    return safe_reports


def solve_pt_two(puzzle: list):
    def difference_in_bound(elem1, elem2):
        return abs(elem1 - elem2) >= 1 and abs(elem1 - elem2) <= 3

    safe_reports = 0
    safe_indexes = []

    for index, report in enumerate(puzzle):
        safe = True
        increasing = report[0] < report[1]

        for i in range(len(report) - 1):
            in_bound = difference_in_bound(report[i], report[i + 1])

            if not in_bound:
                safe = False
                break
            if increasing and report[i] > report[i + 1]:
                safe = False
                break
            if not increasing and report[i] < report[i + 1]:
                safe = False
                break

        if safe:
            safe_reports += 1
            safe_indexes.append(index)

    unsafe_reports = [
        report for j, report in enumerate(puzzle) if j not in safe_indexes
    ]

    def fix_report(report):
        length = len(report)
        for i in range(length):
            tmp_report = [report for j, report in enumerate(report) if j != i]

            safe = True
            increasing = tmp_report[0] < tmp_report[1]

            for i in range(len(tmp_report) - 1):
                in_bound = difference_in_bound(tmp_report[i], tmp_report[i + 1])

                if not in_bound:
                    safe = False
                    break
                if increasing and tmp_report[i] > tmp_report[i + 1]:
                    safe = False
                    break
                if not increasing and tmp_report[i] < tmp_report[i + 1]:
                    safe = False
                    break
            if safe:
                return True

        return False

    for report in unsafe_reports:
        fixable = fix_report(report)
        if fixable:
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    fname = "input.txt"
    puzzle = read_puzzle(fname)
    solutioOne = solve_pt_one(puzzle)
    solutioTwo = solve_pt_two(puzzle)

    print(solutioOne, solutioTwo)
