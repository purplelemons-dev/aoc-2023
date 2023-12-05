from requests import get
from .env import session_cookie, root_dir


def check(day: int):
    "Check if the day exists."
    response = get(
        f"https://adventofcode.com/2023/day/{day}", cookies={"session": session_cookie}
    )
    assert response.status_code == 200, "Invalid day number."
    return str(response.status_code), response.reason


def get_input(day: int, where: str):
    response = get(
        f"https://adventofcode.com/2023/day/{day}/input",
        cookies={"session": session_cookie},
    )
    input_data = response.text
    if day < 10:
        day = "0" + str(day)
    with open(where, "w") as f:
        f.write(input_data)
    return str(response.status_code), response.reason


def get_instructions(day: int, where: str):
    response = get(
        f"https://adventofcode.com/2023/day/{day}", cookies={"session": session_cookie}
    )
    instructions = response.text
    if day < 10:
        day = "0" + str(day)
    with open(where, "w") as f:
        f.write(instructions)
    return str(response.status_code), response.reason


def main(day: int, where: str):
    "Print table of status, write contents to files."
    print("NAME\t\tSTATUS")
    print("input\t\t" + " ".join(get_input(day, where + "/input.txt")))
    print(
        "instructions\t" + " ".join(get_instructions(day, where + "/instructions.html"))
    )
