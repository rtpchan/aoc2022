from aocutil import get_lines
from typing import Tuple



def manhattan_distance(a:Tuple[int,int], b:Tuple[int,int]) -> int:
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def parse(s:str): # -> Tuple(int, int,int,int):
    start = s.find("x=")+2
    end = s.find(", ")
    sx = s[start: end]

    from_index = end
    start = s.find("y=", from_index)+2
    end = s.find(": ", from_index)
    sy = s[start: end]

    from_index = end
    start = s.find("x=", from_index)+2
    end = s.find(", ", from_index)
    bx = s[start: end]

    from_index = end
    start = s.find("y=", from_index)+2
    by = s[start:]

    return int(sx), int(sy), int(bx), int(by)

class Pair:
    def __init__(self, sx, sy, bx, by):
        self.sensor = (sx, sy)
        self.beacon = (bx, by)
        self.dist = manhattan_distance(self.sensor, self.beacon)

    def __str__(self):
        return f"sensor: {self.sensor}, beacon: {self.beacon}, distance: {self.dist}"

def tuning_freq(p):
    return p[0] * 4_000_000 + p[1]

if __name__ == "__main__":

    txt = get_lines("input15_s.txt")

    sensors = []
    min_x = 1e9    # map size
    max_x = -1e9
    min_y = 1e9    # map size
    max_y = -1e9
    for line in txt:
        data = parse(line)
        # print(data)
        if data[0] < min_x:
            min_x = data[0]
        if data[2] < min_x:
            min_x = data[2]
        if data[0] > max_x:
            max_x = data[0]
        if data[2] > max_x:
            max_x = data[2]

        if data[1] < min_y:
            min_y = data[1]
        if data[3] < min_y:
            min_y = data[3]
        if data[1] > max_y:
            max_y = data[1]
        if data[3] > max_y:
            max_y = data[3]
        pair = Pair(*data)
        sensors.append(pair)

    print(f"max x: {max_x}")
    print(f"min x: {min_x}")
    print(f"delta x: {max_x - min_x}")
    print(f"max y: {max_y}")
    print(f"min y: {min_y}")
    print(f"delta y: {max_y - min_y}")
    

    largest_dist = 0
    for s in sensors:
        if s.dist > largest_dist:
            largest_dist = s.dist

    print(f"largest distance: {largest_dist}")

    not_there = 0
    # # vis_arr = []
    # # for y in range(-3, 23):
    vis = ""
    # y = 10  # sample
    y = 2_000_000   # part one input
    for x in range(min_x-largest_dist-2, max_x+largest_dist+2):
        loc = (x, y)
        # print(f"searching {loc}")
        loc_vis = "."
        for s in sensors:
            if s.sensor==loc:
                not_there += 1
                loc_vis = "S"
                break
            if s.beacon==loc:
                loc_vis = "B"
                break
            # if s.sensor != (8,7):  # only check dist for (8,7)
            #     continue           # only for debug
            if manhattan_distance(loc, s.sensor) <= s.dist:
                not_there += 1
                # if s.sensor == (8,7):  # for debug
                loc_vis = "#"
                continue
        vis += loc_vis
    #     # vis_arr.append(vis)

    # print(vis)
    print(f"not there count: {not_there}")
    vis_count = vis.count("#")
    print(f"vis count: {vis_count}")


    # # for line in vis_arr:
    # #     print(line)
    



