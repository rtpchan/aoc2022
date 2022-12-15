from typing import List

def read_file(name : str) -> str:
    with open(name, "r") as file:
        txt = file.read()
    return txt

def get_lines(filename : str) -> List[str]:
    with open(filename, "r") as file:
        txt = file.read()
    return txt.splitlines()
