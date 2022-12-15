from aocutil import get_lines
from typing import Tuple
import pprint


def move_tail(hx:int, hy:int, tx:int, ty:int) -> Tuple[int, int]:
    dx = abs(hx-tx)
    dy = abs(hy-ty)
    if dx + dy > 2:
        if hx > tx:
            tx += 1
        if hx < tx:
            tx -= 1
        if hy > ty:
            ty += 1
        if hy < ty:
            ty -= 1
        return tx, ty
    if dx > 1:
        if hx > tx:
            tx += 1
        if hx < tx:
            tx -= 1
        return tx, ty
    if dy > 1:
        if hy > ty:
            ty += 1
        if hy < ty:
            ty -= 1
        return tx, ty
    return tx, ty

def make_key(x: int, y:int) -> str:
    return f"{x}:{y}"


def show(hx, hy, tx, ty):
    g = [["." for j in range(8)] for i in range(7)]
    g[ty][tx] = "T"
    g[hy][hx] = "H"
    g.reverse()
    pprint.pprint(g)
    print("-------------------")

class Section:
    x = 0
    y = 0

if __name__ == "__main__":
    txt = get_lines("input09.txt") 

    hori = 0  # head coor
    vert = 0
    horit = 0 # tail
    vertt = 0
    # show(hori, vert, horit, vertt)

    grid = {} 
    grid[make_key(horit, vertt)] = True

    for line in txt:
        move = line.split(" ")
        dir = move[0]
        dist = int(move[1])

        # print(dir, dist)
        match dir:
            case "R":
                for d in range(dist):
                    hori += 1
                    m = move_tail(hori, vert, horit, vertt)
                    horit = m[0]
                    vertt = m[1]
                    # show(hori, vert, horit, vertt)
                    grid[make_key(horit, vertt)] = True
            case "L":
                for d in range(dist):
                    hori -= 1
                    m = move_tail(hori, vert, horit, vertt)
                    horit = m[0]
                    vertt = m[1]
                    # show(hori, vert, horit, vertt)
                    grid[make_key(horit, vertt)] = True
            case "U":
                for d in range(dist):
                    vert += 1
                    m = move_tail(hori, vert, horit, vertt)
                    horit = m[0]
                    vertt = m[1]
                    # show(hori, vert, horit, vertt)
                    grid[make_key(horit, vertt)] = True
            case "D":
                for d in range(dist):
                    vert -= 1
                    m = move_tail(hori, vert, horit, vertt)
                    horit = m[0]
                    vertt = m[1]
                    # show(hori, vert, horit, vertt)
                    grid[make_key(horit, vertt)] = True
        
    print(len(grid)) # part one

    # ===== part two
    grid = {} 
    grid[make_key(0, 0)] = True
    rope = [Section() for n in range(10)]

    for line in txt:
        move = line.split(" ")
        dir = move[0]
        dist = int(move[1])

        # print(dir, dist)
        match dir:
            case "R":
                for d in range(dist):
                    rope[0].x += 1
                    for s in range(0, 9, 1):
                        m = move_tail(rope[s].x, rope[s].y, \
                            rope[s+1].x, rope[s+1].y)
                        rope[s+1].x = m[0]
                        rope[s+1].y = m[1]
                    grid[make_key(rope[9].x, rope[9].y)] = True
            case "L":
                for d in range(dist):
                    rope[0].x -= 1
                    for s in range(0, 9, 1):
                        m = move_tail(rope[s].x, rope[s].y, \
                            rope[s+1].x, rope[s+1].y)
                        rope[s+1].x = m[0]
                        rope[s+1].y = m[1]
                    grid[make_key(rope[9].x, rope[9].y)] = True
            case "U":
                for d in range(dist):
                    rope[0].y += 1
                    for s in range(0, 9, 1):
                        m = move_tail(rope[s].x, rope[s].y, \
                            rope[s+1].x, rope[s+1].y)
                        rope[s+1].x = m[0]
                        rope[s+1].y = m[1]
                    grid[make_key(rope[9].x, rope[9].y)] = True
            case "D":
                for d in range(dist):
                    rope[0].y -= 1
                    for s in range(0, 9, 1):
                        m = move_tail(rope[s].x, rope[s].y, \
                            rope[s+1].x, rope[s+1].y)
                        rope[s+1].x = m[0]
                        rope[s+1].y = m[1]
                    grid[make_key(rope[9].x, rope[9].y)] = True

    print(len(grid))