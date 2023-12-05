from sys import argv
from os import system
from . import main, check
from .env import root_dir

try:
    day_number = argv[1]
except IndexError:
    day_number = input("Day: ")

if len(day_number) < 2:
    padded_day = f"0{day_number}"


check(day_number)

system(f"cd {root_dir}/aoc2023 && cp -r ../template ./day{padded_day}")
with open(f"./aoc2023/day{padded_day}/__init__.py", "r") as f:
    x = "".join(
        map(lambda x: x.replace("day = None", f"day = \"{padded_day}\""), f.readlines())
    )
with open(f"./aoc2023/day{padded_day}/__init__.py", "w") as f:
    f.write(x)

main(day=int(day_number), where=f"{root_dir}/aoc2023/day{padded_day}/resources")
