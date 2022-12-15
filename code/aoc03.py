from aoc01 import read_file


letters = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def first(line: str) -> str :
    n = len(line)
    return line[:int(n/2)]

def second(line: str) -> str :
    n = len(line)
    return line[int(n/2):]

def duplicate(a: str, b: str) -> str :
    for c in a:
        for d in b:
            if c==d:
                return c
    return 0

# find duplicate in 3 lines, part 2
def duplicate_three(one : str, two: str, three: str) -> str: 
    for a in one:
        for b in two:
            if a==b:
                for c in three:
                    if b==c:
                        return c
    return "0"

def priority(c : str) -> int :
    try:
        i = letters.index(c)
    except ValueError:
        print(f"cannot find {c}")
        return 0
    return i


if __name__ == "__main__":
    txt = read_file("./input03.txt")

    lines = txt.split("\n")

    sum = 0
    for line in lines[:-1]:
        dupe = duplicate(first(line), second(line))
        pri = priority(dupe)
        sum += pri

    print(sum) # part 1


    sum = 0
    for i in range(0, len(lines)-1, 3):
        one = lines[i]
        two = lines[i+1]
        three = lines[i+2]
        dupe = duplicate_three(one, two, three)
        sum += priority(dupe)

    print(sum)



