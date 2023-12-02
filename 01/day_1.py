"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

"""

import re

def part_1():
    """docstring"""
    calibrated_values = []
    # with open("example.txt", "r") as calibrations:
    with open("input.txt", "r") as calibrations:
        for line in calibrations:
            line = line.strip('\n')

            # Regex patterns
            first_digit = re.search(r'^\D*(\d)', line).group(1)
            last_digit = re.search(r'(\d)\D*$', line).group(1)

            calibrated_values.append(int(str(first_digit+last_digit)))
    # print(sum(calibrated_values), calibrated_values)
    print(sum(calibrated_values))

def part_2():
    pass
    calibrated_values = []
    digits = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
    # with open("example_2.txt", "r") as calibrations:
    with open("input.txt", "r") as calibrations:
        for line in calibrations:
            line = line.strip('\n')

            # Regex patterns
            matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            if str.isdigit(matches[0]):
                first = int(matches[0])
            else:
                first = digits[matches[0]]
            if str.isdigit(matches[-1]):
                second = int(matches[-1])
            else:
                second = digits[matches[-1]]
            calibrated_values.append(first*10+second)
    print(sum(calibrated_values))

def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()