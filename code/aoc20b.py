from typing import List, Set, Tuple

from aocutil import get_lines

class Number:
    def __init__(self, k, n, p=None, f=None):
        self.key = k
        self.n = n
        self.prev_num = p
        self.next_num = f

    def __str__(self):
        return f"{self.n}"
    
    def next(self):
        return self.next_num
    
    def previous(self):
        return self.prev_num


def print_link(d:Number, size:int):
    s = ""

    for n in range(size):
        s += f"{d.n}, "
        d = d.next_num
    print(s)


def move_link(d:Number, size):
    if d.n ==0 :
        return

    # break link
    p = d.prev_num
    n = d.next_num

    # connect next & previous
    p.next_num = n
    n.prev_num = p

    if d.n > 0:
        n1 = d
        for count in range(d.n%(size-1)):
            n1 = n1.next_num
        n2 = n1.next_num
        n2.prev_num = d
        n1.next_num = d
        d.next_num = n2
        d.prev_num = n1

    if d.n < 0:
        n1 = d
        for count in range(-d.n%(size-1)):
            n1 = n1.prev_num
        n2 = n1.prev_num
        n2.next_num = d
        n1.prev_num = d
        d.next_num = n1
        d.prev_num = n2

def find_n(d, count, size):

    one = count % size
    pt = d
    for n in range(one):
        pt = pt.next_num
    return pt.n


if __name__ == "__main__":
    txt = get_lines("input20.txt")

    encrypt = 811589153

    zero_key = 0
    data = {}
    for i, n in enumerate(txt):
        if int(n)==0:
            print(f"found zero, key {i}")
            zero_key = i
        data[i] = Number(i, int(n)*encrypt)
    print(f"zero key: {zero_key}")

    size = len(data)
    data_list = []

    # make link list
    for i in range(size):
        if i==0:
            data[i].next_num = data[i+1]
            data[i].prev_num = data[size-1]
        elif i==size-1:
            data[i].next_num = data[0]
            data[i].prev_num = data[i-1]
        else:
            data[i].next_num = data[i+1]
            data[i].prev_num = data[i-1]
        data_list.append(data[i])

    # print_link(data[0], size)
    for m in range(10):
        for n in range(size):
            move_link(data[n], size)
        # print_link(data[0], size)


    zero = data[zero_key] 

    one = find_n(zero, 1000, size)
    print(one)
    two = find_n(zero, 2000, size)
    print(two)
    three = find_n(zero, 3000, size)
    print(three)
    print(one+two+three)   # 2827 correct


    # # show(data_list)
    # zero_in_list = data_list.index(data[zero_key])
    # print(zero_in_list)

    # one = (zero_in_list + 1000) % len(data)
    # two = (zero_in_list + 2000) % len(data)
    # three = (zero_in_list + 3000) % len(data)
    # print(f"1000th ({one}) = {data_list[one]}")
    # print(f"2000th ({two})= {data_list[two]}")
    # print(f"3000th ({three})= {data_list[three]}")
    # sum = data_list[one].n + data_list[two].n + data_list[three].n
    # print(f"sum = {sum}")  # 5736 wrong -16952 wrong 13774 too high

