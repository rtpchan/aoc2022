from typing import List, Set, Tuple

from aocutil import get_lines


def move(data, i) -> List:
    n = data[i]
    front = data[:i]
    front.extend(data[i+1:])
    front.insert(i+n, n)
    return front

class Number:
    def __init__(self, n):
        self.n = n
#         self.prev_num =   
    def __str__(self):
        return f"{self.n}"

if __name__ == "__main__":
    txt = get_lines("input20.txt")

    data = [int(n) for i, n in enumerate(txt)]
    # data = {i:Number(int(n)) for i, n in enumerate(txt)}

    size = len(data)
    print(size)

    data_set = set(data)
    print(len(data_set))
