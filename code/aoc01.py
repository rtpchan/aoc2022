import sys
from typing import Callable, List


def read_file(name : str) -> str:
    with open(name, "r") as file:
        txt = file.read()
    return txt



def adder() -> Callable[[int], int]:
    sum = 0
    def add(n : int) -> int:
        sum += n
        return sum
    return add

if __name__ == "__main__":
    txt = read_file(sys.argv[1])

    
    pack = []
    temp = 0
    for t in txt.split("\n"):
        try:
            print(t)
            n = int(t)
            temp += n
        except ValueError:
            pack.append(temp)
            temp = 0


    print(pack)
    print( max(pack)) # part one

    pack.sort(reverse=True)
    print(pack)
    print(pack[0], pack[1], pack[2])
    print(pack[0]+ pack[1]+ pack[2]) # part two
