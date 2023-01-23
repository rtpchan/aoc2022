from typing import List, Set, Tuple

from aocutil import get_lines

def solve(txt, name):
    if name=="humn":
        return None
    line = ""
    for l in txt:
        if l[:4]==name:
            line = l
    if line[6:].isnumeric():
        return int(line[6:])
    else:
        op = line[11]
        a = line[6:10]
        b = line[13:17]
        # print(op, a, b)
        try:
            if op=="+":
                return solve(txt, a) + solve(txt, b)
            if op=="-":
                return solve(txt, a) - solve(txt, b)
            if op=="*":
                return solve(txt, a) * solve(txt, b)
            if op=="/":
                return solve(txt, a) / solve(txt, b)
        except TypeError:
            return None

    return None
    
def backtrack(txt, name, target):
    if "humn"==name:
        return target
    line = ""
    left = ""
    right = ""
    for l in txt:
        if l[:4]==name:
            line = l

    if line[6:].isnumeric():
        return int(line[6:])
    else:
        op = line[11]
        left = line[6:10]
        right = line[13:17]

    leftn = solve(txt, left)
    rightn = solve(txt, right)

    print(f"{name} = {left} {op} {right} ~ {leftn} {op} {rightn} ")
    if leftn is None:
        if op=="+":
            return backtrack(txt, left, target - rightn)
        if op=="-":
            return backtrack(txt, left, target + rightn)
        if op=="*":
            return backtrack(txt, left, target / rightn)
        if op=="/":
            return backtrack(txt, left, target * rightn)
    if rightn is None:
        if op=="+":
            return backtrack(txt, right, target - leftn)
        if op=="-":
            return backtrack(txt, right, leftn - target)
        if op=="*":
            return backtrack(txt, right, target / leftn)
        if op=="/":
            return backtrack(txt, right, leftn / target)




    



if __name__ == "__main__":
    txt = get_lines("input21.txt")

    # ======== part one
    # answer = solve(txt, "root")
    # print(answer)

    # ======== part two
    # answer = solve(txt, "sjmn")  # sample pppw = 150
    # print(answer)

    # answer = solve(txt, "zfhn")  # actual jgtb = 46779208742730.0
    # print(answer)


    answer = backtrack(txt, "jgtb", 46779208742730)
    print(answer)

        