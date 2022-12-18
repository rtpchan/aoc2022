from aocutil import get_lines
from aoc17shapes import shapes
from typing import List, Tuple, Set

jet = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

def add_height(top:int, shape: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    new_pos = list.copy(shape)
    for i, s in enumerate(new_pos):
        new_pos[i] = (s[0], s[1]+top + 4)
    return new_pos

def push(jet:str, shape: List[Tuple[int,int]], rock_set:Set) -> List[Tuple[int,int]]: 
    new_pos = list.copy(shape)
    if jet==">":
        for i, s in enumerate(new_pos):
            new_pos[i] = (s[0]+1, s[1])
        for s in new_pos:
            if s[0] == 8 or s in rock_set:
                return shape
        return new_pos
    if jet=="<":
        for i, s in enumerate(new_pos):
            new_pos[i] = (s[0]-1, s[1])
        for s in new_pos:
            if s[0] == 0 or s in rock_set:
                return shape
        return new_pos
    return None

def draw(rock_set:Set, rock:List, height:int):
    col = ["."] * 9
    row = []
    for r in range(height):
        row.append(list.copy(col))
    
    for r in rock_set:
        row[r[1]][r[0]] = "#"
    for r in rock:
        row[r[1]][r[0]] = "@"

    row.reverse()
    for r in row:
        print(r)

def fall(shape: List[Tuple[int,int]], rock_set: Set) -> List[Tuple[int,int]]: 
    new_pos = list.copy(shape)
    for i, s in enumerate(new_pos):
        new_pos[i] = (s[0], s[1]-1)
    for s in new_pos:
        if s in rock_set or s[1]==0:
            # print("matched")
            return shape
    return new_pos

def create_remove_set(high:int, low:int)->Set:
    s = set()
    for y in range(7):
        for x in range(low, high):
            s.add((x,y+1))
    return s


def get_set(rock_set, start, end) -> Set:
    new_set = set()
    for s in rock_set:
        if s[1] <= start and s[1] >= end:
            new_set.add((s[0],s[1]-end))
    return new_set

if __name__ == "__main__":
    # for s in shapes:
    #     print(s)

    # jet = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"  # sample
    jet = get_lines("input17.txt")[0]
    # print(jet)

    print(f"len of jet : {len(jet)}")
    print(f"len of shapes : {len(shapes)}")
    _ = input()

    highest = 0
    rock_set = set()

    next_shape = shapes[0]

    # print("new shape")
    next_shape = add_height(0, next_shape)
    # print(next_shape)

    new_rock = False
    rock_count = 1
    falling = True
    loop_count = 0
    jet_index = 0

    compare_set = set()

    # for n in range(500_000):
    while falling:

        if new_rock:
            # if rock_count%len(shapes)==0 and jet_index==0:

            next_shape = shapes[rock_count%len(shapes)]
            # print(next_shape)
            if rock_count % 100 == 0:
                # print(rock_count)
                temp_set = set.copy(rock_set)

                for s in temp_set:
                    if s[1] < highest-100:
                        rock_set.remove(s)

                if len(compare_set) ==0:
                    compare_set = get_set(rock_set, highest-20, highest-22)
                    print(compare_set)

            if len(compare_set) !=0:
                some_set = get_set(rock_set, highest-20, highest-22)
                if compare_set == some_set:
                    print(some_set)
                    print(f"found match, rock count {rock_count} - {highest}")
                else:
                    pass
                    print(f"not   match, rock count {rock_count} - {highest}")


            # if rock_count == 2022:
            if rock_count == 4700:
            # if rock_count == 1_000_000_000_000:
                falling = False
                # break
            rock_count += 1

            next_shape = add_height(highest, next_shape)
            new_rock = False
        jet_index = loop_count%len(jet)
        # jet_index = n%len(jet)
        loop_count += 1
        # print(jet_index)
        moved = push(jet[jet_index], next_shape, rock_set)
        if moved == next_shape:
            new_set = set(moved)
        # print(moved)
        next_shape = list.copy(moved)

        moved = fall(next_shape, rock_set)
        if moved == next_shape:
            new_set = set(moved)
            rock_set.update(new_set) 
            # print("hit")
            new_rock = True
            for r in moved:
                highest = max(highest, r[1])
        next_shape = list.copy(moved)

        # temp_set = set.copy(rock_set)
        # for s in temp_set:
        #     if s[1] < highest-50:
        #         rock_set.remove(s)

        # remove_set = create_remove_set(highest-100, highest-500)
        # rock_set = rock_set.difference(remove_set)

        
        # draw(rock_set, moved, 28) 
        # print("")
        # _ = input()

    print(f"hightest point {highest}")


    # draw(rock_set, next_shape)
    # next_shape = push(">", next_shape, rock_set)
    # draw(rock_set, next_shape)
    # next_shape = fall(next_shape, rock_set)
    # draw(rock_set, next_shape)

    # print(next_shape)
    


