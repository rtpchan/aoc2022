import aocutil

def check_four(line: str, marker_len: int) -> int:
    start = 0
    char_count = marker_len 

    chars = [*line]  # str to list of char

    for i in range(len(chars)-char_count):
        test_four = set(chars[i:i+char_count])
        if len(test_four) == char_count:
            return i+char_count

    return -1

if __name__ == "__main__":
    
    lines = aocutil.get_lines("input06.txt")

    for line in lines:
        count = check_four(line, 4)
        print(count)    # part one

    for line in lines:
        count = check_four(line, 14)
        print(count)    # part two
