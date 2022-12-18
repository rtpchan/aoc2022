from aocutil import get_lines
from typing import List, Set, Tuple
# import matplotlib.pyplot as plt
# import numpy as np

import sys
sys.setrecursionlimit(10000)

def faces_along_x(cube:List) -> int:
    return cube[1] * cube[2] * 4

def draw_slice(grid):
    for line in grid:
        s = ""
        for char in line:
            s+= char
        print(s)

def next_cube(p)->List:
    return [
        (p[0]+1,p[1],p[2]),
        (p[0]-1,p[1],p[2]),
        (p[0],p[1]+1,p[2]),
        (p[0],p[1]-1,p[2]),
        (p[0],p[1],p[2]+1),
        (p[0],p[1],p[2]-1),
        ]

def in_area(p, edge) -> bool:
    if p[0] < -1 or p[0] > edge:
        return False
    if p[1] < -1 or p[1] > edge:
        return False
    if p[2] < -1 or p[2] > edge:
        return False
    return True

def expand(pos, edge, existing: Set, data_set: Set) -> Set:
    for p in next_cube(pos):
        if in_area(p, edge) and p not in existing and p not in data_set:
            existing.add(p)
            existing = expand(p, edge, existing, data_set)
    return existing





class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xl = None 
        self.xs = None 
        self.yl = None 
        self.ys = None 
        self.zl = None 
        self.zs = None 

    # def add(self, cube):



def create_grid(size_x, size_y):
    grid = []
    for row in range(size_y):
        col = ["."]*size_x
        grid.append(col)
    return grid


if __name__ == "__main__":
    txt = get_lines("input18.txt")

    data = []
    data_set = set()
    for line in txt:
        m = line.split(",")
        data.append(list(map(int, list(m))))
        data_set.add((int(m[0]), int(m[1]), int(m[2])))

    # print(data_set)
    num_face = 0

    outer_set = set()
    # corner = (1,1,1) # sample
    corner = (-1,-1,-1) # actual input
    outer_set.add(corner) # sample

    # edge = 7 # sample
    edge = 22 #  actual input


    # for c in data:
    #     face = 6
    #     # print("=== new cube ===")
    #     # print(c)
    #     for d in data:
    #         if abs(c[0]-d[0]) + abs(c[1]-d[1]) + abs(c[2]-d[2]) == 1:
    #             face -= 1 
    #             # print(d)
    #     num_face += face

    # print(num_face) # Part one

    
    outer_set = expand(corner, edge, outer_set, data_set)

    outer_num = 0
    for c in outer_set:
        face = 6
        # print("=== new cube ===")
        # print(c)
        for d in outer_set:
            if abs(c[0]-d[0]) + abs(c[1]-d[1]) + abs(c[2]-d[2]) == 1:
                face -= 1 
                # print(d)
        outer_num += face

    outer_num = outer_num - (edge+2)*(edge+2) *6
    print(outer_num) # Part two  2570 too low
