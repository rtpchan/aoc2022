import aoc01

match = {
        "A X": 1+3, # X: rock, Y: paper, Z: scissor
        "A Y": 2+6,
        "A Z": 3+0,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 1+6,
        "C Y": 2+0,
        "C Z": 3+3
    }

match2 = {
        "A X": 3+0, # X: lose, Y: draw, Z: win
        "A Y": 1+3,
        "A Z": 2+6,
        "B X": 1+0,
        "B Y": 2+3,
        "B Z": 3+6,
        "C X": 2+0,
        "C Y": 3+3,
        "C Z": 1+6
    }


if __name__ == "__main__":
    txt = aoc01.read_file("input02.txt")


    score = 0
    for line in txt.split("\n")[:-1]:
        score += match[line]

    score_part2 = 0
    for line in txt.split("\n")[:-1]:
        score_part2 += match2[line]

    print(score)  
    print(score_part2)  
