from aocutil import get_lines
from typing import Tuple, List
from collections import deque

height = "SabcdefghijklmnopqrstuvwxyzE"

def print_grid(grid):
    for line in grid:
        print(line)

def check_height(grid, pos) -> int:
    try:
        h = grid[pos[1]][pos[0]]
        return h 
    except IndexError:
        raise "index error"
        # return -99  ## return impossibly high height


def find_lower(grid, pos) -> List[Tuple[int,int]]: 
    row_size = len(grid[0])
    col_size = len(grid)
    h_c = grid[pos[1]][pos[0]]
    h_l = "-"
    h_r = "-"
    h_u = "-"
    h_d = "-"
    good = []
    if pos[0] != 0:
        left = (pos[0]-1, pos[1])
        h_l = check_height(grid, left)
        if (h_c - h_l) <= 1 :
            good.append(left)
    if pos[0] < row_size-1:
        right = (pos[0]+1, pos[1])
        h_r = check_height(grid, right)
        if (h_c - h_r) <= 1:
            good.append(right)
    if pos[1] != 0:
        up = (pos[0], pos[1]-1)
        h_u = check_height(grid, up)
        if (h_c - h_u) <= 1:
            good.append(up)
    if pos[1] < col_size-1:
        down = (pos[0], pos[1]+1)
        h_d = check_height(grid, down)
        if (h_c - h_d) <= 1:
            good.append(down)
    
    # print(h_c, h_l, h_r, h_u, h_d)

    return good


def find_letter(grid, letter):
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            if grid[j][i] == letter:
                return (i, j)
    return None

class Node:
    def __init__(self, coor, parent):
        self.parent = parent
        self.coor = coor
    # def coor(self):Vj
    #     return self.coor

def bfs(grid, start, end):
    q = deque([])  # node
    explored = set()
    q.append(Node(start, None))
    explored.add(start)

    while len(q) != 0:
        v = q.popleft()
        if v.coor == end:
            return v
        next = find_lower(grid, v.coor)
        for n in next:
            if n not in explored:
                explored.add(n)
                new_node = Node(n, v)
                q.append(new_node)

def find_all_a(grid):
    all_a = []
    for j, row in enumerate(grid):
        for i, col in enumerate(row):
            if grid[j][i] == "a":
                all_a.append((i, j))
    return all_a

def count_steps(end_node):
    count = 0
    v = end_node
    while v.parent != None:
        v = v.parent
        count += 1
    return count

if __name__ == "__main__":
    txt = get_lines("input12.txt")

    grid = []
    for line in txt:
        row = []
        for c in line:
            i = height.find(c)
            row.append(i)
        grid.append(row)

    print_grid(grid)
    num_row = len(grid)
    num_col = len(grid[0])

    pos_start = (5, 2)  # coordinates (x, y)
    pos_end = (0,0)


    pos_start = find_letter(txt, "E")
    pos_end = find_letter(txt, "S")

    print(pos_start)
    print(pos_end)

    all_a = find_all_a(txt)

    print("searching")

    end_node = bfs(grid, pos_start, pos_end)
    count = count_steps(end_node)
    print(f"part one : {count}")


    # ========== part two
    lowest = 1e6
    for starting in all_a:
        end_node = bfs(grid, pos_start, starting)
        if end_node is None:
            continue

        count = count_steps(end_node)
        if count < lowest:
            lowest = count
            print(lowest)
    print(f"part two : {lowest}")