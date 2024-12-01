def read_puzzle(fname):
    with open(fname, mode="r", encoding="UTF-8") as f:
        left_list = []
        right_list = []
        for line in f.readlines():
            line = line.strip()
            left_element, right_element = line.split("   ")
            left_list.append(int(left_element))
            right_list.append(int(right_element))
        return left_list, right_list


def solve_pt_one(puzzle):
    left_list, right_list = puzzle
    total_distance = 0
    for _ in range(len(left_list)):
        l_minimum = min(left_list)
        r_minimum = min(right_list)
        left_list.remove(l_minimum)
        right_list.remove(r_minimum)
        total_distance += abs(l_minimum - r_minimum)
    return total_distance


def solve_pt_two(puzzle):
    left_list, right_list = puzzle
    amounts = dict()
    similarity_score = 0

    for left_element in left_list:
        amount = amounts.get(str(left_element))
        if amount is None:
            amount = right_list.count(left_element)
            amounts[str(left_element)] = amount

        similarity_score += left_element * amount

    return similarity_score


if __name__ == "__main__":
    left_list, right_list = read_puzzle("input1.txt")
    # solution_pt_one = solve_pt_one((left_list, right_list))
    solution_pt_two = solve_pt_two((left_list, right_list))
    print(solution_pt_two)
