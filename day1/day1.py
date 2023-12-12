# --- Day 1: Trebuchet?! ---

# Something is wrong with global snow production, and you've been selected to take a look.
# The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;
# the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky")
#  and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky
# ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet
# ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended
#  by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble
#  reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration
#  value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit
#  and the last digit (in that order) to form a single two-digit number.


def find_digits(line):
    # returns all the numbers in the line
    digits = []
    curr = ""
    for i in range(len(line)):
        curr += line[i]

        if line[i].isdigit():
            digits.append(line[i])
            curr = ""

        for key in mapping.keys():
            if key in curr:
                digits.append(mapping[key])
                curr = line[i]

    return digits


def part_one(line):
    first = ""
    last = ""
    for c in line:
        if c.isdigit():
            if first == "":
                first = c
            last = c
    return int(first + last)

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
# one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".


mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def part_two(line):
    digits = find_digits(line)
    first = digits[0]
    last = digits[-1]
    print(f"{line} - {first + last}")

    return int(first + last)


sum = 0
with open('day1-input.txt') as f:
    for line in f:
        # for each line find the first and last digit
        sum += part_two(line.strip())

print(sum)
