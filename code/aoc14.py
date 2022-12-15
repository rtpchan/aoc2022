from aocutil import get_lines
from typing import List, Tuple, Set

# from string 'x,y' to coordinates in tuple(x, y)
def to_coor(a: str) -> Tuple[int, int]:
    c = a.split(",")
    return (int(c[0]), int(c[1]))

def fill_between(a: str, b: str) -> Set[Tuple[int, int]]:
    start = to_coor(a)
    end = to_coor(b)
    line = set()
    if start[0] == end[0]: # same x
        if start[1] < end[1]:
            step = 1
        else:
            step = -1
        for y in range(start[1], end[1], step):
            line.add((start[0], y))
        line.add(end)
        return line
    if start[1] == end[1]: # same y
        if start[0] < end[0]:
            step = 1
        else:
            step = -1
        for x in range(start[0], end[0], step):
            line.add((x, start[1]))
        line.add(end)
        return line
    return line
    
def fill_lines(dataline: str) ->  Set[Tuple[int,int]]:
    points = dataline.split("->")
    num_points = len(points)
    nodes = set()
    for p in range(num_points-1):
        n = fill_between(points[p], points[p+1])
        # print(p, n, points[p], points[p+1])
        for node in n:
            nodes.add(node)
        
    return nodes

def next_pos(rocks: Set[Tuple[int,int]],pos: Tuple[int,int]) -> Tuple[int,int]:
    down = (pos[0], pos[1]+1)
    left = (pos[0]-1, pos[1]+1)
    right = (pos[0]+1, pos[1]+1)

    if down not in rocks:
        return down
    if left not in rocks:
        return left
    if right not in rocks:
        return right
    return pos

def is_off(pos: Tuple[int,int], lowest:int) -> bool:
    if pos[1] > lowest:
        return True
    return False

# drop sand, and return resting place
def drop_sand(rocks: Set[Tuple[int,int]], 
              start: Tuple[int,int], 
              lowest: int) -> Tuple[int,int]:
    current = start
    while 1:
        n = next_pos(rocks, current)
        if is_off(n, lowest): 
            return n
        if n == current:
            return current
        current = n

    return (0,9999999)


if __name__ == "__main__":
    txt = get_lines("input14.txt")

    line_set = set()
    for line in txt:
        line_set.update(fill_lines(line))

    # print(line_set)
    print(f"num of rocks {len(line_set)}")

    lowest = 0  # find lowest point
    for rock in line_set:
        if rock[1] > lowest:
            lowest = rock[1]

    print(f"lowest y coor: {lowest}")

    # count = 0
    # off = False
    # while not off:
    #     p = drop_sand(line_set, (500,0), lowest)
    #     
    #     print(p)
    #     off = is_off(p, lowest)
    #     line_set.add(p)
    #     if not off:
    #         count += 1

    # print(count)  # part one

    floor = lowest + 2

    # add floor
    line_set.update(fill_between(f"0, {floor}",f"1000,{floor}"))

    count = 0
    off = False
    while not off:
        p = drop_sand(line_set, (500,0), lowest)
        
        # print(p)
        off = is_off(p, floor)
        line_set.add(p)
        if not off:
            count += 1
        if p == (500,0):
            break

    print(count)  # part one
