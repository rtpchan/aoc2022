from aocutil import get_lines
from typing import Tuple, List



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

def in_boundary(p:Tuple[int,int], minx,miny,maxx, maxy)->bool:
    if p[0] < minx or p[0] > maxx or \
        p[1] < miny or p[1] > maxy:
        return False
    return True

# generate boundary just outside the becon distance
def gen_boundary(sensor, distance) -> List[Tuple[int,int]]:
    dist = distance + 1
    path  = []
    # north
    north = (sensor[0], sensor[1]+dist)
    for i in range(dist):
        n = (north[0]+1, north[1]-1)
        path.append(n)
        north = n
    # east
    east = north
    for i in range(dist):
        n = (east[0]-1, east[1]-1)
        path.append(n)
        east = n
    # south
    south = east
    for i in range(dist):
        n = (south[0]-1, south[1]+1)
        path.append(n)
        south = n
    # west
    west = south
    for i in range(dist):
        n = (west[0]+1, west[1]+1)
        path.append(n)
        west = n
    return path
    
    
    


if __name__ == "__main__":

    txt = get_lines("input15.txt")

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
    vis_arr = []
    ys_min = 0
    # ys_max = 20
    ys_max = 4_000_000
    xs_min = 0
    # xs_max = 20
    xs_max = 4_000_000

    becon = None
    for s in sensors:
        for n in gen_boundary(s.sensor, s.dist):
            if in_boundary(n, xs_min, ys_min, xs_max, ys_max):
                loc_vis = "."
                for s in sensors:
                    # search just ouside the parameter
                    if s.sensor==n:
                        loc_vis = "S"
                        break
                    if s.beacon==n:
                        loc_vis = "B"
                        break
                    # if s.sensor != (8,7):  # only check dist for (8,7)
                    #     continue           # only for debug
                    if manhattan_distance(n, s.sensor) <= s.dist:
                        # if s.sensor == (8,7):  # for debug
                        loc_vis = "#"
                        continue
                if loc_vis==".":
                    print(n)
                    becon = n
                    break
            if becon is not None:
                break
        if becon is not None:
            break
    if becon is None:
        print("not found")
    else:
        print(tuning_freq(becon))

    

        



