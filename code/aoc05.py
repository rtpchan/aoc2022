from aoc01 import read_file
from typing import List


def create_stack(lines : List[str])-> List[str]:
    
    stack = []
    for i in range(9):
        stack.append([])

    for line in lines.split("\n")[:-1]:
        if "[" in line:
            stack_count = 0
            for i in range(1, 50, 4):
                if i > len(line):
                    continue
                if line[i]!=" ":
                    stack[stack_count].append(line[i])
                stack_count += 1
        else:
            # stack info ended
            for s in stack:
                s = s.reverse()  # reverse so i can append and pop
            return stack
    return stack

# move one crate
def move_one(stack: List[str], fr: int, to: int) -> List[str]:
    crate = stack[fr-1].pop() 
    stack[to-1].append(crate)
    return stack

def move_9001(stack: List[str], num: int, fr: int, to: int) -> List[str]:
    if num < 1:
        return stack
    temp = []
    for n in range(num):
        temp.append(stack[fr-1].pop())
    temp.reverse()
    stack[to-1].extend(temp)
    return stack


def process_move(stack : List[str], line : str) -> List[str]:
    if line.startswith("move"):
        num = int(line[5:7])
        fr = int(line[line.find("t")-2])
        to = int(line[-1])
        for n in range(num):
            s=  move_one(stack, fr, to)
        return s
    else:
        return stack

def process_move_9001(stack: List[str], line: str) -> List[str]:
    if line.startswith("move"):
        num = int(line[5:7])
        fr = int(line[line.find("t")-2])
        to = int(line[-1])
        s=  move_9001(stack, num, fr, to)
        return s
    else:
        return stack



if __name__ == "__main__":

    txt = read_file("./input05.txt")
    stack = create_stack(txt)

    # print(stack)

    for line in txt.split("\n")[:-1]:
        stack = process_move(stack, line)

    top = ""
    for col in stack:
        if len(col) > 0:
            top += col[-1]

    print(top) # part one

    stack = create_stack(txt)

    # print(stack)

    for line in txt.split("\n")[:-1]:
        stack = process_move_9001(stack, line)

    top = ""
    for col in stack:
        if len(col) > 0:
            top += col[-1]
    
    print(top) # part two 
