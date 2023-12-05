from .. import root_dir

day = "01"

with open(f"{root_dir}/aoc2023/day{day}/resources/input.txt", "r") as f:
    data = list(filter(bool, map(str.strip, f.readlines())))


def part1(data=data, *args, **kwargs):
    # we need to get the first and last digits per line and add total
    total = 0
    for line in data:
        numbers = list(filter(str.isnumeric, line))
        print(numbers)
        sub_total = int(f"{numbers[0]}{numbers[-1]}")
        total += sub_total
        print(sub_total)
    return total


def part2(*args, **kwargs):
    spelt = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    new = []
    new = "\n".join(data)
    for k, v in spelt.items():
        new = new.replace(k,f"{k}{v}{k}")
    new = new.split("\n")

    return part1(data=new)
