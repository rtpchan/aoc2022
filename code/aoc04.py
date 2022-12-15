from aoc01 import read_file
from typing import Tuple

def separate(line : str) -> Tuple[int,int,int,int]:
    two_elves = line.split(",")
    e1 = two_elves[0].split("-")
    e2 = two_elves[1].split("-")
    return int(e1[0]), int(e1[1]), int(e2[0]), int(e2[1])

def is_included(a:int, b:int, c:int, d:int) -> bool :
    if a <= c and b >= d:
        return True 
    if a >= c and b <= d:
        return True
    return False

def is_overlap(a:int, b:int, c:int, d:int) -> bool :
    if b >= c and a <= d:
        return True 
    if d >= a and c <= b:
        return True
    return False

if __name__ == "__main__":
    txt = read_file("./input04.txt")

    count = 0
    for line in txt.split("\n")[:-1]:
        d = separate(line)
        included = is_included(*d)
        if included:
            count += 1

    print(count)  # part one

    count = 0
    for line in txt.split("\n")[:-1]:
        d = separate(line)
        overlap = is_overlap(*d)
        if overlap:
            count += 1

    print(count) # part two

