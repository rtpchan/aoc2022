from aocutil import get_lines
from typing import List, Callable

class Monkey:
    def __init__(self, items, op, div, nt, nf):
        self.items = items
        self.op = op
        self.div = div
        self.next_true = nt
        self.next_false = nf
        self.inspect_count = 0

    def add(self, s : int):
        self.items.append(s)

    def process(self, monkeys):
        for i in self.items:
            self.inspect_count += 1
            w = self.op(i)
            w = int(w / 3)
            if (w % self.div) ==0:
                monkeys[self.next_true].add(w)
            else:
                monkeys[self.next_false].add(w)
        self.items = []

    def process2(self, monkeys):
        for i in self.items:
            self.inspect_count += 1
            w = self.op(i)
            # w = int(w / 3) # not divide by 3 in part 2
            if w > 9699690**2: 
                w = w % 9699690
                # w = w % 96577 # for sample
            if (w % self.div) ==0:
                monkeys[self.next_true].add(w)
            else:
                monkeys[self.next_false].add(w)
        self.items = []

def parse_data(txt: List[str]) -> Monkey:
    monkey_id = txt[0][7]
    items = []
    # print(txt[1][txt[1].find(":")+1:])
    for n in txt[1][txt[1].find(":")+1:].split(","):
        items.append(int(n))    # items line
    op = txt[2][23]
    term = txt[2][24:].strip()
    f = lambda x: x
    if op=="*":
        if term.isnumeric():
            f = lambda x : x * int(term)
        else :
            f = lambda x : x * x
    if op=="+":
        if term.isnumeric():
            f = lambda x : x + int(term)
        else :
            f = lambda x : x + x
    
    div = int(txt[3][21:].strip())
    nt = int(txt[4][29].strip())
    nf = int(txt[5][30:].strip())
    # print(items, op, term, div, nt, nf)
    return Monkey(items, f, div, nt, nf)


if __name__ == "__main__":
    txt = get_lines("input11.txt")

    monkeys = []

    data = []
    for line in txt:
        if line != "":
            data.append(line)
        else:
            monkeys.append(parse_data(data))
            data = []
    monkeys.append(parse_data(data))


    for i in range(20):
        for m in monkeys:
            m.process(monkeys)



    for m in monkeys:
        print(m.items)

    counts = []
    for m in monkeys:
        counts.append(m.inspect_count)

    counts.sort(reverse=True)
    print(counts)
    print(counts[0] * counts[1])

# ========= part two ===============
    print("==== Part Two ====")

    monkeys = []

    data = []
    for line in txt:
        if line != "":
            data.append(line)
        else:
            monkeys.append(parse_data(data))
            data = []
    monkeys.append(parse_data(data))


    for i in range(10_000):
        for m in monkeys:
            m.process2(monkeys)

    for m in monkeys:
        print(m.items)
        
    counts = []
    for m in monkeys:
        counts.append(m.inspect_count)
    print(counts)

    counts.sort(reverse=True)
    # print(counts)
    print(counts[0] * counts[1])