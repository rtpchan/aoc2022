from typing import List, Set, Tuple

from aocutil import get_lines

class Elf:
    def __init__(self, coor):
        self.coor = coor
        self.propose = None
        self.direction = ["N", "S", "W", "E"]
        self.duplicated = False

    def rotate(self):
        new_dir = list.copy(self.direction[1:4])
        new_dir.append(self.direction[0])
        self.direction = list.copy(new_dir)

    def plan(self, grid):
        c = self.coor
        # n = grid[c[0]-1][c[1]]
        # ne = grid[c[0]-1][c[1]+1]
        # e = grid[c[0]][c[1]+1]
        # se = grid[c[0]+1][c[1]+1]
        # s = grid[c[0]+1][c[1]]
        # sw = grid[c[0]-1][c[1]-1]
        # w = grid[c[0]][c[1]-1]
        # nw = grid[c[0]-1][c[1]-1]
        n = (c[0]-1,c[1])
        ne = (c[0]-1,c[1]+1)
        e = (c[0],c[1]+1)
        se = (c[0]+1,c[1]+1)
        s = (c[0]+1,c[1])
        sw = (c[0]-1,c[1]-1)
        w = (c[0],c[1]-1)
        nw = (c[0]-1,c[1]-1)

        dir = None
        for d in self.direction:
            if d=="N":
                if self.__has_elf(grid, nw) or self.__has_elf(grid, n) or self.__has_elf(grid, ne):
                    continue
                else:
                    dir = d
                    break
            if d=="E":
                if self.__has_elf(grid, ne) or self.__has_elf(grid, e) or self.__has_elf(grid, se):
                    continue
                else:
                    dir = d
                    break
            if d=="S":
                if self.__has_elf(grid, se) or self.__has_elf(grid, s) or self.__has_elf(grid, sw):
                    continue
                else:
                    dir = d
                    break
            if d=="W":
                if self.__has_elf(grid, sw) or self.__has_elf(grid, w) or self.__has_elf(grid, nw):
                    continue
                else:
                    dir = d
                    break
        self.propose = dir    

    def __has_elf(self, grid, coor):
        g = grid[coor[0]][coor[1]] 
        if g != None:
            return g
        return False

    def new_pos(self):
        if self.propose == "N":
            return (self.coor[0]-1, self.coor[1])
        if self.propose == "S":
            return (self.coor[0]+1, self.coor[1])
        if self.propose == "E":
            return (self.coor[0], self.coor[1]+1)
        if self.propose == "W":
            return (self.coor[0], self.coor[1]-1)
        return self.coor

    def duplicate(self):
        self.duplicate = True
        
    def reset(self):
        if self.propose is not None and not self.duplicate:
            self.rotate()
            self.coor = self.new_pos()
        self.duplicate = False
        self.propose = None


def has_elf(grid, coor):
    g = grid[coor[0]][coor[1]] 
    if g != None:
        return g
    return False


def show(grid):
    for row in grid:
        s = ""
        for col in row:
            s += col
        print(s)

def empty_grid(size):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(None)
        grid.append(row)
    return grid

if __name__ == "__main__":
    txt = get_lines("input23_s.txt")

    pad = 4

    grid = empty_grid(7+pad*2)
    for i, row in enumerate(txt):
        for j, col in enumerate(row):
            if col=="#":
                grid[i][j] = Elf((i+pad,j+pad))

    proposed_grid = empty_grid(7+pad*2)
    for i, row in enumerate(grid):
        r = []
        for j, col in enumerate(row):
            if col is not None:
                col.plan(grid)
                c = col.new_pos()
                g = has_elf(proposed_grid, c)
                if g is not None:
                    g.duplicate()
                    col.duplicate()
                proposed_grid[c[0]][c[1]] = col

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col is not None:
                col.reset()

    next_grid = empty_grid(7+pad*2)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col is not None:
                c = col.coor
                next_grid[c[0]][c[1]] = col

    show(next_grid)
            

    # show(txt)



