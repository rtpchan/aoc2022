
from aocutil import get_lines
from typing import List, Set, Tuple
from pulp import *
from aoc19pulp import problem

class Blueprint:
    def __init__(self, id, o, c, oo, oc, go, gc):
        self.id = id
        self.o = o
        self.c = c
        self.oo = oo
        self.oc = oc
        self.go = go
        self.gc = gc

    def __str__(self):
        return f"{self.id}, {self.o}, {self.c}, {self.oo}, {self.oc}, {self.go}, {self.gc}"

if __name__ == "__main__":

    data = []
    for line in get_lines("input19.txt"):
        # print(line)
        id = int(line[line.find("rint ")+4:line.find(":")])
        os = line.find("osts ")+4
        o = int(line[os:line.find("ore.")])
        cs = line.find("osts ", os) + 4
        c = int(line[cs:line.find("ore.", cs)])
        oos = line.find('osts ', cs) + 4
        oo = int(line[oos: line.find('ore and', oos)])
        ocs = line.find('and ')+4
        oc = int(line[ocs: line.find('clay.')])
        gos = line.rfind("osts ")+4
        go = int(line[gos: line.rfind('ore')])
        gcs = line.rfind('and ')+4
        gc = int(line[gcs: line.rfind('obsidian')])

        b = Blueprint(id, o, c, oo, oc, go, gc)
        data.append(b)

    # for bp in data:
    #     print(bp)

    ## ========  PART ONE ===========
    # geode_count = []

    # for d in data:
    #     count = problem(d.o, d.c, d.oo, d.oc, d.go, d.gc, 25)
    #     geode_count.append(count)


    # print(geode_count)

    # sum = 0
    # for i, g in enumerate(geode_count):
    #     sum += (i+1)*g

    # print(f"Qaulity levels sum: {sum}")

    ## ========  PART TWO ===========
    d = data[0]
    count0 = problem(d.o, d.c, d.oo, d.oc, d.go, d.gc, 33)
    d = data[1]
    count1 = problem(d.o, d.c, d.oo, d.oc, d.go, d.gc, 33)
    d = data[2]
    count2 = problem(d.o, d.c, d.oo, d.oc, d.go, d.gc, 33)

    print(count0, count1, count2)
    print(count0*count1*count2)



