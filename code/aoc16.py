from aocutil import get_lines
from typing import List

#======= NOT WORKING IN ACTUAL INPUT========

class Room:
    def __init__(self, name:str, rate:int, connect:List[str]):
        self.name = name
        self.rate = rate
        self.connect = connect  # list of connection
        self.open = False
        self.released = 0
    
    def  __str__(self) -> str:
        return f"{self.name} rate={self.rate} lead to {self.connect}"

    def value(self, time_left : int) -> int:
        return time_left * self.rate


def parse(line : str) -> Room:
    name = line[6:8]
    rate = int(line[line.find("=")+1:line.find(";")])
    connect = line[line.rfind("valve")+6:].split(",")
    connect = list(map(str.strip, connect))
    return Room(name, rate, connect)

def release(rooms : List[Room]) -> int:
    total = 0
    for r in rooms:
        if r.open:
            total += r.rate
            r.released += r.rate
    return total

class Node:
    def __init__(self, pos:Room, open_valve: bool, parent:str, time_to_end:int):
        self.name = pos.name
        self.valve_opened = open_valve
        self.next_actions = []  # open valve or move to next node
        self.children = []
        self.parent = parent
        self.time_to_end = time_to_end
        
        # calc value before valve open check, prevent double dip
        if parent is not None:
            parent_value = parent.value
        else: 
            parent_value = 0
        self.value = parent_value + self.valve_opened * pos.rate * time_to_end

        self.__is_valve_opened() # check if valve opened previously, toggle if true
        self.next_actions = list.copy(pos.connect)
        if pos.rate > 0 and self.valve_opened==False:
            self.next_actions.append("OV")
        
    def __is_valve_opened(self): # check if 
        if self.valve_opened:
            return
        node = self.parent
        while node is not None:
            if node.name == self.name and node.valve_opened==True:
                self.valve_opened = True
                return
            node = node.parent
        return


    def add_child(self, node):
        self.children.append(node)

    def __str__(self):
        return f"{self.name}:{self.value}"

def search_value(root:Node, name:str) -> int:
    max_value = -1 
    for c in root.children:
        if c.name == name:
            # print(f"name matched {name}")
            # print(c.value, max_value)
            if c.value > max_value:
                max_value = c.value
        child_value = search_value(c, name)
        if child_value > max_value:
            max_value = child_value
    return max_value




if __name__ == "__main__":
    txt = get_lines("input16_s.txt")

    rooms = {}
    for line in txt:
        r = parse(line)
        rooms[r.name] = r

    for r in rooms.values():
        print(r)


    # value_table = []  # [time][location]
    # for time in range(1,31,1):
    #     rooms_value = []
    #     for r in rooms:
    #         rooms_value.append(r.value(30-time))
    #     value_table.append(rooms_value)

    # for line in value_table:
    #     print(line)

    # root = Node(rooms["AA"], False, None, 31)  # sample
    root = Node(rooms["AA"], False, None, 30)  # part one
    # print(root.name)
    # print(root.next_actions)
    # print(root.valve_opened)
    # print(root.value)
    # print(root.time_to_end)

    parent = [root]
    final = []
    for time in range(29, 0,-1):
        print(f"==== time {time} =====")
        child_list = []
        for p in parent:
            print(f"----- parent {p.name} ----")
            print(f"actions: {p.next_actions}")
            for a in p.next_actions:
                print(a)
                better = False
                if a =="OV":
                    child = Node(rooms[p.name], True, p, time)
                    better = True
                else:
                    child = Node(rooms[a], False, p, time)
                    if child.value >= search_value(root, child.name):
                        better = True
                if better:
                    p.add_child(child)
                    child_list.append(child)
                    print(f"{a} - {child.value}")
            # _ = input()
        parent = list.copy(child_list)
        # for c in child_list:
        #     print(c)
        final = list.copy(child_list)

    max_value = 0
    best_route = None
    for n in final:
        if n.value > max_value:
            max_value = n.value
            best_route = n
        print(f"{n.name} - {n.value}")

    print(max_value)

    n = best_route
    route = []
    while n is not None:
        route.append(n)
        n = n.parent

    route.reverse()
    for i, node in enumerate(route):
        print(f"{i+1} - {node.name} - {node.value}")


    # b = Node(rooms["BB"], False, root, 29)
    # print(b.name)
    # print(b.next_actions)
    # print(b.valve_opened)
    # print(b.value)
    # print(b.time_to_end)
    # root.add_child(b)

    # b2 = Node(rooms["BB"], True, b, 28)  # "OV is an option"
    # print(b.name)
    # print(b.next_actions)
    # print(b.valve_opened)
    # print(b.value)
    # print(b.time_to_end)
    # b.add_child(b2)
    

    # c = Node(rooms["CC"], False, b2, 27)
    # print(c.name)
    # print(c.next_actions)
    # print(c.valve_opened)
    # print(c.value)
    # print(c.time_to_end)
    # b2.add_child(c)

    # c = Node(rooms["CC"], True, b, 26)
    # print(c.name)
    # print(c.next_actions)
    # print(c.valve_opened)
    # print(c.value)
    # print(c.time_to_end)


    # print("search value")
    # v = search_value(root, "BB")
    # print(v)
    # v = search_value(root, "CC")
    # print(v)