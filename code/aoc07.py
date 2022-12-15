from aocutil import get_lines
from typing import Dict, Tuple, List

def set_item(fs: Dict, path: str, item: Dict) -> Dict:
    path_split = path.split("/")
    cwd = fs
    for n in path_split[1:]:
        if n in cwd:
            cwd = cwd[n]
        else:
            cwd[n] = {}
            cwd = cwd[n]
    cwd.update(item)
    return fs

def dir_size(fs: Dict) -> int:
    size = 0
    for key, value in fs.items():
        if type(value) is dict:
            size += dir_size(value)
        else:
            size += value
    return size

# process command, return file system and current directory 
def process_command(fs: Dict, cwd: str, line: str) -> Tuple[(Dict, str)]:
    if line.startswith("$"):
        words = line.split(" ")
        if words[1]=="cd":
            if words[2] =="..":
                i = cwd.rfind("/")
                cwd = cwd[:i]
                return fs, cwd
            elif words[2] == "/":
                return fs, "/"
            else:
                # assume input is always correct
                cwd += f"/{words[2]}" 
                return fs, cwd
        elif words[1] =="ls":
            return fs, cwd
        else:
            # command not found
            return fs, cwd
    if line[0].isdigit():
        words = line.split(" ")
        fs = set_item(fs, cwd, {words[1]:int(words[0])})
        return fs, cwd
    if line.startswith("dir"):
        return fs, cwd
    raise SyntaxError(line)



    


if __name__ == "__main__":
    lines = get_lines("input07.txt")

    # print(lines)

    cwd = "/"
    fs = {}

    for line in lines:
        o = process_command(fs, cwd, line)
        fs = o[0]
        cwd = o[1]


    size = 0
    def get_sum(fs: Dict):
        global size
        for key, value in fs.items():
            if type(value) is dict:
                s = dir_size(value)
                if s < 100_000:
                    size += s
                get_sum(value)
            
    get_sum(fs)
    print(size)  # part one

    used_space = dir_size(fs)
    print(f"used space: {used_space}")
    disk_space = 70_000_000
    free_space = disk_space - used_space
    print(f"free space: {free_space}")
    required_space = 30_000_000
    needed_space = required_space - free_space
    print(f"to be deleted: {needed_space}")


    size = 1e12
    def find_folder(fs: Dict):
        global size
        for key, value in fs.items():
            if type(value) is dict:
                s = dir_size(value)
                # print(key, s)
                if s > needed_space and s < size:
                    size = s
                find_folder(value)
    
    find_folder(fs)
    print(size) # part two
    # size_list.sort()
    # print(size_list)
