from typing import List, Set, Tuple

from aocutil import get_lines

# NOT STARTED WORKING ON IT

def parse_map_line(line:str) -> List[str]:
    col = []
    for c in line:
        col.append(c)
    return col

def parse_steps(line:str) -> List[str]:
    line += "X"
    steps = []
    last_index = 0
    for i, c in enumerate(line):
        if c.isalpha():
            steps.append(line[last_index:i+1])
            last_index = i+1
    
    return steps

def starting_loc(grid) -> Tuple[int, int]:
    for i, j in enumerate(grid[0]):
        if j==".":
            return (0,i)

def change_dir(current:str, command:str) -> str:
    if command=="L":
        match current:
            case "N":
                return "W" 
            case "W":
                return "S" 
            case "S":
                return "E" 
            case "E":
                return "N" 
    elif command=="R":
        match current:
            case "N":
                return "E" 
            case "W":
                return "N" 
            case "S":
                return "W" 
            case "E":
                return "S" 
    else:
        return current

def next_coor(dir, coor) -> Tuple[int,int]:
    match dir:
        case "N":
            return (coor[0]-1, coor[1])
        case "E":
            return (coor[0], coor[1]+1)
        case "S":
            return (coor[0]+1, coor[1])
        case "W":
            return (coor[0], coor[1]-1)
    return None

def char_at(grid, coor)-> str:
    if coor[0] < 0 or coor[1] < 0:
        return ""
    try:
        return grid[coor[0]][coor[1]]
    except IndexError:
        return ""
    
def show(grid):
    for row in grid:
        s = ""
        for col in row:
            s += col
        print(s)

def wrap_around(grid, coor, dir) -> Tuple[int,int]:

    match dir:
        case "E":
            next_coor = (coor[0], 0)
            nc = char_at(grid, next_coor)
            while nc == "" or nc == " ":
                next_coor = (next_coor[0], next_coor[1]+1)
                nc = char_at(grid, next_coor)
            return next_coor
        case "W":
            next_coor = (coor[0], len(grid[0])-1)
            while char_at(grid, next_coor) == "" or char_at(grid, next_coor) == " ":
                next_coor = (next_coor[0], next_coor[1]-1)
            return next_coor
        case "N":
            next_coor = (len(grid)-1, coor[1])
            while char_at(grid, next_coor) == "" or char_at(grid, next_coor) == " ":
                next_coor = (next_coor[0]-1, next_coor[1])
            return next_coor
        case "S":
            next_coor = (0, coor[1])
            while char_at(grid, next_coor) == "" or char_at(grid, next_coor) == " ":
                next_coor = (next_coor[0]+1, next_coor[1])
            return next_coor
    return None 

def run(grid, instructions, coor) :

    dir = "E"
    for ins in instructions:
        print(ins)
        count = int(ins[:-1])
        for c in range(count):
            print(f"current pos {coor} -> {dir}")
            nm = next_coor(dir, coor)
            nc = char_at(grid, nm)
            print(f"check {nm} -- {nc}")
            if nc == "" or nc == " ":
                nm, dir = wrap_around(grid, nm, dir)
                nc = char_at(grid, nm)
                print(f"wrap around to {nm} -- {nc}")
            if nc == "#": # wall
                print(f"hit wall, next dir {ins[-1]}")
                # dir = change_dir(dir, ins[-1])
                break
            if nc == "." or nc == ">" or nc == "v" or nc == "<" or nc =="^":  # valid move
                print(nm, dir)
                # match dir:
                #     case "E":
                #         grid[coor[0]][coor[1]] = ">"
                #     case "S":
                #         grid[coor[0]][coor[1]] = "v"
                #     case "W":
                #         grid[coor[0]][coor[1]] = "<"
                #     case "N":
                #         grid[coor[0]][coor[1]] = "^"
                coor = nm
                continue
            else:
                print(f"some other tiles - {nm} --{nc}--")
                raise TypeError("ahhh")
        dir = change_dir(dir, ins[-1])
        print(f"turning {ins[-1]} to {dir}")
        
    return coor, dir, grid



def password(coor, dir) ->  int:
    sum = (coor[0]+1) * 1000 + (coor[1]+1) * 4
    if dir == "E":
        return sum
    if dir == "S":
        return sum + 1
    if dir == "W":
        return sum + 2
    if dir == "N":
        return sum + 3
    return 0

def which_face(pos) :
    x = pos[0]     # .   y --->
    y = pos[1]     # .   x
    # sample       # .   V
    if y >= 8 and y < 12 and x >=0 and x < 4:
        return "top"
    if y >= 8 and y < 12 and x >=4 and x < 8:
        return "front"
    if y >= 8 and y < 12 and x >=8 and x < 12:
        return "bottom"
    if y >= 12 and y < 16 and x >=8 and x < 12:
        return "right"
    if y >= 4 and y < 8 and x >=4 and x < 8:
        return "left"
    if y >= 0 and y < 4 and x >=4 and x < 8:
        return "back"
    raise KeyError("off the face") 

    



if __name__ == "__main__":
    txt = get_lines("input22_s.txt")

    grid = []   # map[row][col]
    steps = []
    parse_map = True
    for line in txt:
        if line=="":
            parse_map = False
        if parse_map:
            col = parse_map_line(line)
            grid.append(col)
        else:
            steps = parse_steps(line)

    set_top = 

    start = starting_loc(grid)
    print(start)


    # result, dir, new_grid = run(grid, steps, start)
    # pw = password(result, dir)
    # print(result, dir)
    # print(pw)   # 67238 too low 81250 wrong   114370 too highg

    # show(new_grid)
