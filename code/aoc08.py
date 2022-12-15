from typing import List
import pprint

from aocutil import get_lines


def to_list(s : str) -> List[int]:
    n = []
    for c in s:
        n.append(int(c))
    return n


# looking from top side
def from_top(trees: List[List[int]], vis: List[List[int]],
             ) -> List[List[int]]:

    no_col = len(trees[0])
    max_height = [-1 for _ in range(no_col)]
    for i, row in enumerate(trees):
        for j, col in enumerate(row):
            if col > max_height[j]:
                vis[i][j] = True
                max_height[j] = col
    return vis

# looking from bottom side
def from_bottom(trees: List[List[int]], vis: List[List[int]],
             ) -> List[List[int]]:

    no_col = len(trees[0])
    no_row = len(trees)
    trees.reverse()
    max_height = [-1 for _ in range(no_col)]
    for i, row in enumerate(trees):
        for j, col in enumerate(row):
            if col > max_height[j]:
                vis[no_row-1-i][j] = True
                max_height[j] = col
    trees.reverse()
    return vis

# looking from left side
def from_left(trees: List[List[int]], vis: List[List[int]],
             ) -> List[List[int]]:

    no_col = len(trees[0])
    no_row = len(trees)
    for i, row in enumerate(trees):
        max_height = -1
        for j, col in enumerate(row):
            if col > max_height:
                vis[i][j] = True
                max_height = col
    return vis

# looking from right side
def from_right(trees: List[List[int]], vis: List[List[int]],
             ) -> List[List[int]]:

    no_col = len(trees[0])
    no_row = len(trees)
    for i, row in enumerate(trees):
        row.reverse()
        max_height = -1
        for j, col in enumerate(row):
            if col > max_height:
                vis[i][no_row-1-j] = True
                max_height = col
        row.reverse()
    return vis

def count_up(trees: List[List[int]], i: int, j: int) -> int :
    height = trees[i][j]
    index = i-1
    count = 0
    while index >= 0:
        count += 1
        if trees[index][j] >= height :
            return count
        else:
            index -= 1
    return count

def count_down(trees: List[List[int]], i: int, j: int) -> int :
    height = trees[i][j]
    index = i+1
    count = 0
    while index < len(trees):
        count += 1
        if trees[index][j] >= height :
            return count
        else:
            index += 1
    return count

def count_left(trees: List[List[int]], i: int, j: int) -> int :
    height = trees[i][j]
    index = j-1
    count = 0
    while index >= 0:
        count += 1
        if trees[i][index] >= height :
            return count
        else:
            index -= 1
    return count

def count_right(trees: List[List[int]], i: int, j: int) -> int :
    height = trees[i][j]
    index = j+1
    count = 0
    while index < len(trees[0]):
        count += 1
        if trees[i][index] >= height :
            return count
        else:
            index += 1
    return count

def scenic_score(trees: List[List[int]], i: int, j: int) -> int :
    up = count_up(trees, i, j)
    down = count_down(trees, i, j)
    left = count_left(trees, i, j)
    right = count_right(trees, i, j)
    return up * down * left * right

if __name__ == "__main__":
    txt = get_lines("input08.txt")

    mat = [to_list(s) for s in txt]
    # pprint.pprint(mat)

    visible = [[False for c in r] for r in mat]

    no_row = len(mat)
    no_col = len(mat[0])

    visible = from_top(mat, visible)
    visible = from_bottom(mat, visible)
    visible = from_left(mat, visible)
    visible = from_right(mat, visible)

    # pprint.pprint(visible)

    count = 0
    for i, row in enumerate(visible):
        for j, col in enumerate(row):
            if col:
                count += 1
    print(count)

    highest_score = 0
    for i, row in enumerate(mat):
        for j, col in enumerate(row):
            n = scenic_score(mat, i, j)
            if n > highest_score:
                highest_score = n

    print(highest_score)