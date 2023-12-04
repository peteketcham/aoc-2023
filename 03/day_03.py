"""

"""

import re


def part_1():
    """
    """
    total = 0
    with open("input.txt", "r") as file:
        engine_schematic = file.readlines()
        engine_schematic = [line.rstrip("\n") for line in engine_schematic]

    for row_number, line in enumerate(engine_schematic):
        # Find all matches of numbers and their indices
        matches = [(match.group(), match.start()) for match in re.finditer(r'\d+', line)]
        for number, index in matches:
            # symbol above number
            a = bool(re.search(r'[^0-9.]', engine_schematic[max(0, row_number - 1)][max(0, index - 1): index + len(number) + 1]))
            # print(engine_schematic[max(0, row_number - 1)][max(0, index - 1): index + len(number) + 1])

            # symbol before or after number
            b = bool(re.search(r'[^0-9.]', line[max(0, index - 1): index + len(number) + 1]))
            # print(line[max(0, index - 1): index + len(number) + 1])

            # symbol below number
            try:
                c = bool(re.search(r'[^0-9.]', engine_schematic[row_number + 1][max(0, index - 1): index + len(number) + 1]))
                # print(engine_schematic[row_number + 1][max(0, index - 1): index + len(number) + 1])
            except IndexError as e:
                c = False

            # print(int(number), a, b, c)
            # print()

            if (a or b or c):
                total += int(number)
    print(total)

def part_2():
    """
    """
    total = 0
    with open("input.txt", "r") as file:
        engine_schematic = file.readlines()
        engine_schematic = [line.rstrip("\n") for line in engine_schematic]
    stars = []
    number_matches = []
    for row_number, line in enumerate(engine_schematic):
        # Find all * and their indices
        stars += [(row_number, match.start()) for match in re.finditer(r'\*', line)]
        number_matches += [(int(match.group()), row_number, set(range(match.start(), match.start() + len(match.group())))) for match in re.finditer(r'\d+', line)]
    for star in stars:
        rows = [y for y in number_matches if star[0] - 1  <= y[1] <= star[0] + 1]
        # print(rows)
        adjacent = [x for x in rows if x[2] & set(range(star[1] - 1, star[1] + 2))]
        if len(adjacent) == 2:
            total += adjacent[0][0] * adjacent[1][0]
    print(total)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
