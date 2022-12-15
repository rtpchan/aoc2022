from aocutil import read_file
from typing import List
import json
import functools

def is_list(s:str) -> bool:
    if s.startswith("["):
        return True
    return False

def is_left_smaller(left: List, right: List) -> bool:
    if len(left) == 0:
        left = [0]
    if len(right) == 0:
        right = [0]
    # _ = input()
    for l, r in zip(left, right):
        # print(l)
        # print(r)
        # print("===")
        if type(l)==int and type(r)==int:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                continue
        else: 
            if type(l)==int:
                l = [l] 
            if type(r)==int:
                r = [r]
            b = is_left_smaller(l, r)
            if b is not None:
                return b
            continue
    if len(left) < len(right):
        return True
    if len(left) == len(right):
        return None
    return False

def find_first_num(ar: List) -> int:
    if len(ar) == 0:
        return 0
    one = ar[0]
    if type(one)==int:
        return one
    return find_first_num(one)

def compare(one, two):
    o = find_first_num(one)
    t = find_first_num(two)
    if o < t:
        return -1
    if o == t:
        if len(one) < len(two):
            return -1
    return 1

if __name__ == "__main__":

    input_file = read_file("input13.txt")
    txt = input_file.split("\n\n")

    msg = []

    for line in txt:
        pair = line.splitlines()
        msg.append(pair)




    sum = 0
    for index, pair in enumerate(msg):
        
        left = msg[index][0]
        right = msg[index][1]

        left = json.loads(left)
        right = json.loads(right)
            
        b = is_left_smaller(left, right)
        if b:
            sum += (index+1)
        print(index+1 ,b)

    print(sum)   # PART ONE

    all = []


    for index, pair in enumerate(msg):
        
        left = msg[index][0]
        right = msg[index][1]

        left = json.loads(left)
        right = json.loads(right)

        all.append(left)
        all.append(right)
    
    all.append([[2]])
    all.append([[6]])

    all = sorted(all, key=functools.cmp_to_key(compare))

    prod = 1
    for i, a in enumerate(all):
        if a==[[2]] or a==[[6]]:
            prod *= (i+1)

        first = find_first_num(a)
        print(f"{i+1} - {first} -  {a}")

    print(prod)   # Part two  // sorting not working correctly
    # answer is 127 * 207 = 26289