from aocutil import get_lines

def signal_strength(cycle: int, reg: int) -> int:
    if cycle in [20,60,100,140,180,220]:
        # print(cycle,  reg)
        return cycle * reg
    return 0

def show_screen(display:str):
    for n in range(1, 240, 40):
        print(display[n-1:n+39])

def draw_pixel(cycle: int, reg: int)-> str:
    # print(cycle, reg, abs(cycle-reg) <2)
    cycle = cycle % 40
    if cycle==0:
        cycle=40
    pixel_pos = cycle - 1
    if abs(pixel_pos - reg) <2 :
        return "#"
    else:
        return "."

if __name__ == "__main__":
    txt = get_lines("input10.txt")

    reg = 1
    cycle = 0
    signal_sum = 0

    for line in txt:
        if line.startswith("addx"):
            com = line.split(" ")
            v = int(com[1])

            cycle += 1
            signal_sum += signal_strength(cycle, reg)
            
            cycle += 1
            signal_sum += signal_strength(cycle, reg)

            reg += v

        if line.startswith("noop"):

            cycle += 1
            signal_sum += signal_strength(cycle, reg)

    print(signal_sum)  # Part one


    screen = ""
    reg = 1
    cycle = 0

    for line in txt:
        # if cycle > 21:
        #     break
        if line.startswith("addx"):
            com = line.split(" ")
            v = int(com[1])

            cycle += 1
            screen += draw_pixel(cycle, reg)
            cycle += 1
            screen += draw_pixel(cycle, reg)

            reg += v
        if line.startswith("noop"):

            cycle += 1
            screen += draw_pixel(cycle, reg)


    show_screen(screen)           
    #  if abs(cycle - reg) <2 :
    #             screen += "#"
    #         else:
    #             screen += "."